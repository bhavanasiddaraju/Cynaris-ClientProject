
from pathlib import Path
import sys

from fastapi import FastAPI, HTTPException, Query

ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = ROOT / "artifacts"

# Make the src directory importable.
sys.path.insert(0, str(ROOT))

from src.recommend import EduTrackRecommender

app = FastAPI(
    title="EduTrack LMS Recommendation API",
    description="Personalized subject recommendations for students.",
    version="1.0.0",
)

recommender = None


@app.on_event("startup")
def load_recommender():
    global recommender

    required_files = [
        "predicted_scores.csv",
        "interaction_matrix.csv",
        "popularity_baseline.csv",
    ]

    missing = [
        name for name in required_files
        if not (ARTIFACTS_DIR / name).exists()
    ]

    if missing:
        raise RuntimeError(
            "Model artifacts missing: "
            + ", ".join(missing)
            + ". Run python -m src.train first."
        )

    recommender = EduTrackRecommender(
        artifacts_dir=ARTIFACTS_DIR
    )


@app.get("/")
def home():
    return {
        "message": "EduTrack LMS Recommendation API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": recommender is not None,
    }


@app.get("/recommend/{student_id}")
def get_recommendations(
    student_id: str,
    top_n: int = Query(default=5, ge=1, le=10),
):
    if recommender is None:
        raise HTTPException(
            status_code=503,
            detail="Recommendation model is not loaded.",
        )

    try:
        results = recommender.recommend(
            student_id=student_id,
            top_n=top_n,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Recommendation failed: {exc}",
        ) from exc

    return {
        "student_id": student_id,
        "count": len(results),
        "recommendations": results,
    }
