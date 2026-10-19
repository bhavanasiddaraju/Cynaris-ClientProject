
from pathlib import Path
import streamlit as st
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.recommend import EduTrackRecommender

ARTIFACTS_DIR = ROOT / "artifacts"

st.set_page_config(
    page_title="EduTrack LMS",
    page_icon="🎓",
    layout="wide",
)

@st.cache_resource
def load_recommender():
    return EduTrackRecommender(artifacts_dir=ARTIFACTS_DIR)


st.title("🎓 EduTrack LMS")
st.subheader("Adaptive Learning Path Recommendations")
st.write(
    "Discover suggested subjects based on student engagement patterns."
)

try:
    recommender = load_recommender()
except FileNotFoundError:
    st.error(
        "Model artifacts were not found. Generate them by running "
        "`python -m src.train` after placing the engagement CSV at "
        "`data/raw/aiml_content_engagement.csv`."
    )
    st.stop()
except Exception as exc:
    st.error(f"Could not load the recommender: {exc}")
    st.stop()

student_id = st.text_input(
    "Enter Student ID",
    placeholder="e.g. STU-00029",
)

top_n = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5,
)

if st.button("Get Recommendations", type="primary"):
    if not student_id.strip():
        st.warning("Please enter a student ID.")
    else:
        results = recommender.recommend(
            student_id=student_id.strip(),
            top_n=top_n,
        )

        if not results:
            st.info(
                "No unseen subjects are available to recommend "
                "for this student."
            )
        else:
            st.success(
                f"Generated {len(results)} recommendations."
            )

            st.caption(
                "Confidence scores are normalized ranking scores, "
                "not probabilities."
            )

            for rank, item in enumerate(results, start=1):
                with st.container(border=True):
                    col1, col2, col3 = st.columns([1, 3, 2])

                    col1.metric("Rank", rank)
                    col2.subheader(item["recommended_subject"])
                    col3.metric(
                        "Confidence score",
                        f'{item["confidence_score"]:.2f}',
                    )

                    st.progress(
                        max(
                            0.0,
                            min(1.0, item["confidence_score"]),
                        )
                    )

                    st.caption(
                        f'Method: {item["recommendation_method"]} '
                        f'| Predicted score: {item["predicted_score"]:.4f}'
                    )

st.divider()
st.caption(
    "EduTrack LMS · Prototype recommendations are subject-level; "
    "individual course IDs are not available in the supplied dataset."
)
