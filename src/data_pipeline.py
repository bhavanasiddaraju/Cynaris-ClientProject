
from pathlib import Path
import pandas as pd


def load_engagement_data(csv_path):
    """Load and validate student-content engagement data."""
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Engagement dataset not found: {csv_path}"
        )

    df = pd.read_csv(csv_path)

    required_columns = {
        "student_id",
        "subject",
        "engagement_score",
    }

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    df = df.dropna(
        subset=["student_id", "subject", "engagement_score"]
    ).copy()

    df["student_id"] = df["student_id"].astype(str)
    df["subject"] = df["subject"].astype(str)
    df["engagement_score"] = pd.to_numeric(
        df["engagement_score"], errors="coerce"
    )

    df = df.dropna(subset=["engagement_score"])

    if df.empty:
        raise ValueError("No valid engagement records found.")

    return df


def build_interaction_matrix(df):
    """Aggregate engagement into a student-by-subject matrix."""
    matrix = df.pivot_table(
        index="student_id",
        columns="subject",
        values="engagement_score",
        aggfunc="mean",
        fill_value=0,
    )

    return matrix.sort_index().sort_index(axis=1)


def build_popularity_baseline(df):
    """Calculate average engagement for each subject."""
    popularity = (
        df.groupby("subject")["engagement_score"]
        .mean()
        .sort_values(ascending=False)
    )

    return popularity


if __name__ == "__main__":
    data_path = Path("data/raw/aiml_content_engagement.csv")

    engagement = load_engagement_data(data_path)
    interactions = build_interaction_matrix(engagement)
    popularity = build_popularity_baseline(engagement)

    print("Engagement records:", len(engagement))
    print("Students:", interactions.shape[0])
    print("Subjects:", interactions.shape[1])
    print("\nMost popular subjects:")
    print(popularity.head())
