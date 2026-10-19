
from pathlib import Path
import pandas as pd


class EduTrackRecommender:
    def __init__(self, artifacts_dir="edutrack_artifacts"):
        self.artifacts_dir = Path(artifacts_dir)

        self.scores = pd.read_csv(
            self.artifacts_dir / "predicted_scores.csv",
            index_col=0
        )
        self.interactions = pd.read_csv(
            self.artifacts_dir / "interaction_matrix.csv",
            index_col=0
        )
        self.popularity = pd.read_csv(
            self.artifacts_dir / "popularity_baseline.csv",
            index_col=0
        ).iloc[:, 0]

        self.scores.index = self.scores.index.astype(str)
        self.interactions.index = self.interactions.index.astype(str)

    def recommend(self, student_id, top_n=5, seen_subjects=None):
        student_id = str(student_id)
        seen = set(seen_subjects or [])

        if student_id in self.interactions.index:
            row = self.interactions.loc[student_id]
            seen.update(row[row > 0].index.tolist())

        if student_id in self.scores.index:
            ranked = self.scores.loc[student_id].drop(
                labels=list(seen), errors="ignore"
            ).sort_values(ascending=False)
            method = "matrix_factorization"
        else:
            ranked = self.popularity.drop(
                labels=list(seen), errors="ignore"
            ).sort_values(ascending=False)
            method = "popularity_fallback"

        ranked = ranked.head(top_n)

        if len(ranked) and ranked.max() > ranked.min():
            confidence = (ranked - ranked.min()) / (
                ranked.max() - ranked.min()
            )
        else:
            confidence = pd.Series(0.5, index=ranked.index)

        return [
            {
                "student_id": student_id,
                "recommended_subject": subject,
                "predicted_score": round(float(ranked[subject]), 4),
                "confidence_score": round(float(confidence[subject]), 4),
                "recommendation_method": method
            }
            for subject in ranked.index
        ]
