# EduTrack LMS — Week 3 Baseline Report

## Objective
Establish an initial recommendation benchmark by comparing
matrix factorization with a popularity-based baseline.

## Data and preprocessing
- Source: aiml_content_engagement.csv
- Students in interaction matrix: 459
- Subjects: 10
- Interaction values: Mean engagement scores
- Missing interactions: Filled with zero
- Model: TruncatedSVD
- Components: 2
- Random seed: 42

## Evaluation methodology
Deterministic leave-one-subject-out

Eligible students evaluated: 110

One observed subject was held out per eligible student.
Recommendations were ranked among subjects not observed
in that student's training interactions.

## Results

| Metric | Matrix Factorization | Popularity Baseline |
|---|---:|---:|
| NDCG@10 | 0.4825 | 0.5081 |
| NDCG@5 | 0.3516 | 0.3828 |
| Hit Rate@5 | 0.6000 | 0.6182 |

## Acceptance target
Required NDCG@10: 0.55

Matrix factorization target achieved: False

The initial matrix-factorization model has not met the target.
The popularity baseline currently performs better under this
evaluation procedure.

## Limitations and next steps
- Tune model parameters and investigate ranking improvements.
- Validate the evaluation procedure with additional experiments.
- The current prototype recommends subjects rather than
  individual courses because individual course IDs are unavailable
  in the supplied engagement dataset.
- Confidence scores are normalized ranking scores, not calibrated
  probabilities.

## Conclusion
The initial data pipeline, baseline models, and recommendation API
have been implemented and tested. This report establishes the
initial benchmark; further optimization is required to meet the
NDCG@10 target.
