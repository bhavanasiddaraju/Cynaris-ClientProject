# Evaluation Plan — EduTrack LMS

## 1. Purpose

This document defines the evaluation strategy for the EduTrack LMS adaptive learning path recommendation system.

The objective is to measure recommendation quality, compare candidate models fairly, verify cold-start behavior, and assess application performance against the project acceptance criteria.

## 2. Primary Metric: NDCG@10

Normalized Discounted Cumulative Gain at 10 (NDCG@10) measures the quality of a ranked recommendation list by considering the relevance of recommended items and their positions.

Relevant courses ranked near the top contribute more than equally relevant courses ranked lower.

**Acceptance target:** NDCG@10 ≥ 0.55 on the held-out test set.

This is a target, not a result. It will be reported as achieved only if the implemented evaluation confirms it.

## 3. Dataset Validation

Before training, the pipeline will inspect the provided datasets:

- `aiml_student_performance.csv`
- `aiml_content_engagement.csv`
- `aiml_edtech_tests.json`

Validation will identify available student identifiers, course identifiers, timestamps, engagement signals, completion information, course metadata, missing values, and duplicate records where applicable.

The evaluation labels and relevance definition will be selected based on the actual schema and documented before final model comparison.

## 4. Data Splitting

The data will be divided into training, validation, and test sets.

Where timestamps are available and appropriate, a chronological split will be considered to simulate recommending courses using only information available before the evaluation period.

Where a chronological split is not possible, a reproducible split will be used with a fixed random seed.

Records from the test set must not be used to train the model or select its hyperparameters. Preprocessing steps that learn from data must be fitted using training data only.

## 5. Baseline Model

A simple baseline will be established before evaluating the primary model.

Depending on the dataset, the baseline may recommend popular courses or courses with high historical engagement.

The baseline score and evaluation procedure will be recorded so that more complex models can be compared against it.

## 6. Model Comparison

At least two configurations of the primary recommendation model will be trained and compared.

For each experiment, record:

- Model and algorithm.
- Hyperparameter configuration.
- Training and validation setup.
- NDCG@10.
- Other applicable ranking metrics.
- Training duration.
- Notes on limitations or unexpected behavior.

MLflow will be used to track experiments and their metrics.

The best configuration will be selected using validation performance and then evaluated on the held-out test set.

## 7. Additional Quality Metrics

Where the dataset supports them, the project will also report:

- Precision@10.
- Recall@10.
- Recommendation coverage.
- Number of eligible recommendations returned.
- Performance for students with different amounts of interaction history.

The relevance definition and metric implementation will be kept consistent across model comparisons.

## 8. Cold-Start Evaluation

The system will be tested with:

1. A student who has sufficient historical interactions.
2. A student with little interaction history.
3. A student with no usable interaction history.
4. A course with insufficient interaction history, if applicable.

The tests will verify that the system uses an appropriate content-based or other documented fallback when collaborative filtering cannot produce reliable personalized recommendations.

The fallback behavior and any limitations caused by missing metadata will be documented.

## 9. Serving Performance

The integrated application will be evaluated against these acceptance criteria:

| Requirement | Target or check |
|---|---|
| Ranking quality | NDCG@10 ≥ 0.55 on the test set |
| Dashboard responsiveness | Recommendations rendered in under 1 second |
| Cold-start | Suitable fallback is available |
| Load testing | Test with 50 concurrent requests |
| Integration | Automated tests pass for the serving workflow |
| Retraining | Repeatable model retraining pipeline is available |

Latency measurements will state the test environment, request type, and measurement method. Dashboard rendering time and API response time will be recorded separately where possible.

Load testing will document observed latency, throughput, errors, and test configuration rather than assuming the system meets the target.

## 10. Reproducibility

The project will record relevant package versions, random seeds, model configurations, data-splitting strategy, and evaluation results.

The same evaluation code and relevance definition will be used for comparable experiments.

## 11. Reporting Results

The baseline report and final model report will include:

- Dataset summary and preprocessing decisions.
- Evaluation methodology.
- Baseline and candidate model results.
- Selected model configuration and supporting evidence.
- Cold-start test results.
- Serving performance measurements.
- Limitations and potential sources of bias.

No metric will be reported as a measured result until the corresponding experiment has been executed.

## 12. Current Status

This document establishes the evaluation plan. Dataset-specific choices and measured performance will be finalized
