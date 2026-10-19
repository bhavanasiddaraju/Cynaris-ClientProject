# EduTrack LMS — Adaptive Learning Path Recommendation System

 1. Project Overview

EduTrack LMS is an AI/ML project that aims to provide personalized learning path recommendations to students based on their performance and content engagement.

The system will recommend the next five relevant courses for a student using collaborative filtering and a content-based fallback for cold-start scenarios.

 2. Problem Statement

Students have different learning needs, interests, performance levels, and engagement patterns. A generic course sequence may not suit every learner.

This project aims to develop an adaptive recommendation system that identifies relevant learning opportunities and provides personalized course recommendations.

 3. Project Objectives

- Build a collaborative filtering recommendation model using matrix factorization.
- Develop a content-based fallback for new students and other cold-start scenarios.
- Evaluate recommendation quality using NDCG@10, targeting at least 0.55.
- Serve recommendations through a REST API using FastAPI.
- Develop a Streamlit dashboard displaying the next five recommended courses and their scores.
- Achieve dashboard response time below one second.
- Design an A/B testing strategy for evaluating recommendation quality.
- Implement a repeatable model retraining pipeline.
- Test the integrated application and evaluate performance under 50 concurrent requests.

 4. Provided Datasets

The project brief provides three data packs:

1. `aiml_student_performance.csv`
2. `aiml_content_engagement.csv`
3. `aiml_edtech_tests.json`

The actual schemas, column meanings, missing values, and relationships between these files will be inspected before preprocessing and model development.

Raw datasets will not be committed to GitHub without appropriate permission.

 5. Proposed Technology Stack

- Python
- Pandas and NumPy
- Scikit-Surprise for matrix factorization, subject to data compatibility
- Scikit-learn for preprocessing and content-based methods
- FastAPI for the REST API
- Streamlit for the recommendation dashboard
- MLflow for experiment tracking
- Pytest for automated testing
- Git and GitHub for version control and collaboration

 6. Proposed System Architecture

The system will follow these stages:

1. Data ingestion and validation.
2. Data cleaning and preprocessing.
3. Construction of student-course interactions.
4. Baseline recommendation model and evaluation.
5. Collaborative filtering using matrix factorization.
6. Hyperparameter experiments and model selection.
7. Content-based fallback for cold-start students or items.
8. Recommendation ranking and top-five selection.
9. FastAPI integration and Streamlit dashboard.
10. Automated testing, load testing, and model retraining.
11. Continuous integration and final model documentation.

 7. Evaluation Metrics and Acceptance Criteria

| Metric | Project target |
|---|---|
| NDCG@10 | At least 0.55 |
| Dashboard response time | Below 1 second |
| Recommendations | Five relevant courses per student |
| Cold-start | Content-based fallback |
| Experiment tracking | At least two hyperparameter configurations |
| Load testing | 50 concurrent requests |
| A/B testing | Documented experimental design |
| Retraining | Repeatable pipeline |
| Final delivery | Demo, model card, deployment guide, and passing CI |

These are target requirements. Actual performance will be measured and reported after implementation.

 8. Milestone Roadmap

### Week 1 — Research and Architecture Design
Review three relevant papers or repositories, define the architecture and evaluation metrics, and establish the project repository and data pipeline skeleton.

### Week 3 — Data Pipeline and Baseline Model
Implement data ingestion and preprocessing, train a baseline model, establish evaluation benchmarks, and prepare a baseline report.

### Week 6 — Core Model and Experimentation
Train the primary recommendation model with at least two hyperparameter configurations, track experiments using MLflow or Weights & Biases, and document the best configuration with evidence.

### Week 9 — Integration and Testing
Integrate the model with FastAPI or Streamlit, write integration tests, and conduct load testing with 50 concurrent requests. Document latency and throughput.

### Week 12 — Final Demo and Model Card
Record a five-minute end-to-end demonstration, complete the model card and bias audit, document deployment, and submit the final code with passing continuous integration checks.

 9. Initial Repository Structure


Cynaris-ClientProject/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── research.md
│   ├── architecture.md
│   ├── evaluation_plan.md
│   └── ab_testing.md
├── data/
│   └── README.md
├── src/
│   └── data_pipeline.py
├── tests/
├── experiments/
├── reports/
├── models/
├── api/
├── dashboard/
└── .github/
    └── workflows/


Additional implementation files will be added as the project progresses.

 10. Responsible Data Handling

- Follow the client's data access and redistribution permissions.
- Do not commit API keys, passwords, or credentials.
- Avoid exposing personal student information in reports or demonstrations.
- Evaluate the system for potential recommendation bias and limitations.
- Document data limitations and model assumptions.

 11. Current Status

Week 1: Initial project documentation and architecture planning.

Implementation status and evaluation results will be updated as each milestone is completed.
