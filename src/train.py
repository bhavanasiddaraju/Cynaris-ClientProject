
from pathlib import Path
import json

import joblib
import pandas as pd
from sklearn.decomposition import TruncatedSVD

from src.data_pipeline import (
    load_engagement_data,
    build_interaction_matrix,
    build_popularity_baseline,
)


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "raw" / "aiml_content_engagement.csv"
ARTIFACTS_DIR = ROOT / "artifacts"


def train_model(n_components=2):
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    engagement = load_engagement_data(DATA_PATH)
    interactions = build_interaction_matrix(engagement)
    popularity = build_popularity_baseline(engagement)

    # SVD requires at least two students and two subjects.
    if min(interactions.shape) < 2:
        raise ValueError(
            "At least two students and two subjects are required."
        )

    # Keep the component count valid for this dataset.
    components = min(
        n_components,
        min(interactions.shape) - 1
    )

    model = TruncatedSVD(
        n_components=components,
        random_state=42
    )

    latent_scores = model.fit_transform(interactions)
    reconstructed = latent_scores @ model.components_

    predicted_scores = pd.DataFrame(
        reconstructed,
        index=interactions.index,
        columns=interactions.columns,
    )

    interactions.to_csv(
        ARTIFACTS_DIR / "interaction_matrix.csv"
    )
    popularity.to_csv(
        ARTIFACTS_DIR / "popularity_baseline.csv",
        header=["mean_engagement"]
    )
    predicted_scores.to_csv(
        ARTIFACTS_DIR / "predicted_scores.csv"
    )
    joblib.dump(
        model,
        ARTIFACTS_DIR / "matrix_factorization_model.joblib"
    )

    metadata = {
        "model": "TruncatedSVD",
        "n_components": components,
        "random_state": 42,
        "n_students": int(interactions.shape[0]),
        "n_subjects": int(interactions.shape[1]),
        "n_interactions": int(len(engagement)),
        "explained_variance_ratio_sum": float(
            model.explained_variance_ratio_.sum()
        ),
        "item_unit": "subject",
        "limitation": (
            "The supplied engagement data identifies subjects, "
            "not individual courses. Recommendations are subject-level."
        ),
    }

    with open(
        ARTIFACTS_DIR / "model_metadata.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(metadata, file, indent=2)

    print("Training completed.")
    print("Students:", interactions.shape[0])
    print("Subjects:", interactions.shape[1])
    print("SVD components:", components)
    print(
        "Explained variance:",
        round(metadata["explained_variance_ratio_sum"], 4)
    )
    print("Artifacts saved to:", ARTIFACTS_DIR)


if __name__ == "__main__":
    train_model(n_components=2)
