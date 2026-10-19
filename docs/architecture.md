# System Architecture — EduTrack LMS

## 1. Project Overview

EduTrack LMS is an adaptive learning path recommendation system that recommends the next five courses for a student based on available student-course interactions and course information.

The system will use Python for data processing and model training, a recommendation service for generating predictions, FastAPI for REST API access, and Streamlit for the interactive dashboard.

## 2. High-Level Architecture

```text
Client-Provided Datasets
          |
          v
Data Ingestion and Validation
          |
          v
Preprocessing and Feature Engineering
          |
          v
Train / Validation / Test Split
          |
          v
Baseline Recommendation Model
          |
          v
Matrix-Factorization Model
          |
          v
Offline Model Evaluation
          |
          v
Save Selected Model and Artifacts
          |
          v
Recommendation Service
          |
          +--------------------+
          |                    |
          v                    v
     FastAPI REST API    Streamlit Dashboard
          |                    |
          +---------+----------+
                    |
                    v
        Top 5 Course Recommendations
          with Confidence/Ranking Scores
```

A content-based recommendation fallback will support students or courses for which collaborative interaction history is insufficient.

## 3. Main Components

### 3.1 Data Ingestion

The pipeline will load the client-provided datasets:

- `aiml_student_performance.csv`
- `aiml_content_engagement.csv`
- `aiml_edtech_tests.json`

The pipeline will inspect column names, data types, missing values, duplicate records, student identifiers, course identifiers, and interaction fields.

The JSON file will be inspected to establish its intended role before it is incorporated into training or testing.

### 3.2 Preprocessing and Feature Engineering

The preprocessing component will:

- Validate the input schema.
- Handle missing and duplicate records appropriately.
- Identify available student-course interactions.
- Transform suitable engagement signals into model inputs when justified by the data.
- Prepare course metadata for content-based recommendations.
- Create leakage-aware training and evaluation splits.

The exact transformations will be finalized after inspecting the datasets.

### 3.3 Recommendation Models

**Baseline model**

A simple recommendation strategy will establish an initial performance benchmark. Depending on the available data, this may use popular or frequently engaged-with courses.

**Primary model**

A matrix-factorization or collaborative-filtering model will learn from student-course interactions. The specific algorithm will be selected based on whether the data contains explicit ratings or implicit behavioral feedback.

At least two hyperparameter configurations will be evaluated during model experimentation.

### 3.4 Cold-Start Fallback

Collaborative filtering may struggle when a student or course has little or no interaction history.

A content-based fallback will use available course metadata and student information, where suitable, to identify relevant courses. If student-specific information is unavailable, a popularity-based fallback may be used.

The system will avoid recommending courses that the student has already completed or interacted with when the available data supports reliable filtering.

### 3.5 Recommendation Service

A reusable Python service will accept a student identifier and return up to five ranked course recommendations.

Each recommendation will include:

- Course identifier.
- Ranking or model score.
- Recommendation method used, such as collaborative filtering or fallback.

Model scores will not automatically be described as calibrated probabilities. Any confidence interpretation will be documented according to how the score is calculated.

### 3.6 FastAPI REST API

FastAPI will expose an endpoint for requesting recommendations.

The API will validate the student identifier, call the recommendation service, and return structured JSON results. Integration tests will verify successful requests and appropriate handling of invalid inputs.

### 3.7 Streamlit Dashboard

The dashboard will allow a user to select or enter a student identifier and view the next five recommended courses with their scores.

The interface will display useful feedback when a student has insufficient history or no eligible courses are available.

The target is to render recommendations in less than one second under the agreed test conditions.

### 3.8 Experiment Tracking and Retraining

MLflow will be used to record model configurations, evaluation metrics, and experiment results.

A repeatable retraining pipeline will load and validate data, train the model, evaluate it, and save the resulting artifacts. A model should only be promoted when it satisfies the defined evaluation checks.

### 3.9 Testing and Continuous Integration

The project will include:

- Data validation tests.
- Recommendation-service tests.
- Cold-start tests.
- API integration tests.
- Evaluation-metric tests.
- Load testing with 50 concurrent requests.
- A CI workflow that runs the project's automated tests.

## 4. Evaluation Strategy

NDCG@10 will be the primary ranking metric, with an acceptance target of at least 0.55 on the test set.

Additional measurements will include:

- Precision@10 or Recall@10 where relevant to the available labels.
- Recommendation coverage.
- Cold-start fallback behavior.
- API latency and throughput.
- Dashboard response time.

Evaluation results will be reported only after the relevant experiments have been run.

## 5. Proposed Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Data processing | Pandas, NumPy |
| Recommendation modelling | Surprise or a suitable alternative based on the data |
| Content-based fallback | Scikit-learn |
| REST API | FastAPI |
| Interactive dashboard | Streamlit |
| Experiment tracking | MLflow |
| Automated tests | Pytest |
| Version control | Git and GitHub |
| CI | GitHub Actions |

## 6. Repository Organization

```text
Cynaris-ClientProject/
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── docs/
│   ├── research.md
│   ├── architecture.md
│   ├── evaluation_plan.md
│   └── ab_testing.md
├── src/
│   ├── data_pipeline.py
│   ├── train.py
│   ├── recommend.py
│   └── evaluate.py
├── api/
│   └── main.py
├── dashboard/
│   └── app.py
├── tests/
├── experiments/
├── models/
├── reports/
└── .github/
    └── workflows/
```

This is the intended organization. Files will be added as their corresponding components are implemented.

## 7. Implementation Roadmap

- **Week 1:** Research, architecture, evaluation planning, and initial repository/data-pipeline setup.
- **Week 3:** Dataset ingestion, preprocessing, baseline model, and benchmark report.
- **Week 6:** Primary model, hyperparameter experiments, and experiment tracking.
- **Week 9:** API and dashboard integration, automated tests, and 50-concurrent-request load testing.
- **Week 12:** End-to-end demonstration, model card, bias audit, deployment guide, and CI verification.

## 8. Current Status

This document describes the proposed architecture. Model selection, data transformations, measured metrics, and performance claims will be confirmed through implementation and testing.
