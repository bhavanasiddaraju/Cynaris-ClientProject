# Research Review — EduTrack LMS

## 1. Introduction

EduTrack LMS is an adaptive learning path recommendation system designed to recommend relevant courses to students based on their previous learning activity and course engagement.

This review examines three research papers and one implementation reference to guide the system architecture and model selection.

## 2. Research Paper 1: Matrix Factorization Techniques for Recommender Systems

**Authors:** Yehuda Koren, Robert Bell, and Chris Volinsky  
**Published:** 2009, IEEE Computer  
**Link:** https://doi.org/10.1109/MC.2009.263

### Key findings
- Matrix factorization represents students and courses using latent factors.
- These factors help identify patterns in student-course interactions.
- Regularization can help reduce overfitting.

### Relevance to EduTrack LMS

Matrix factorization is a candidate for the primary recommendation model. It can learn student preferences from historical interactions and generate personalized course recommendations.

The final algorithm will depend on the structure and type of feedback available in the supplied datasets.

## 3. Research Paper 2: Collaborative Filtering for Implicit Feedback Datasets

**Authors:** Yifan Hu, Yehuda Koren, and Chris Volinsky  
**Published:** 2008, IEEE International Conference on Data Mining  
**Link:** https://doi.org/10.1109/ICDM.2008.22

### Key findings
- User behavior can provide implicit preference signals.
- Interaction strength and confidence can be important when learning from implicit feedback.
- The absence of an interaction does not necessarily mean that a user dislikes an item.

### Relevance to EduTrack LMS

The supplied content-engagement dataset may contain behavioral signals rather than explicit ratings. We will inspect the dataset before deciding how to transform those signals into recommendation training data.

The preprocessing pipeline must not automatically treat every missing student-course interaction as a negative preference.

## 4. Research Paper 3: Neural Collaborative Filtering

**Authors:** Xiangnan He and colleagues  
**Published:** 2017, Proceedings of the 26th International Conference on World Wide Web  
**Link:** https://doi.org/10.1145/3038912.3052569

### Key findings
- Neural collaborative filtering models user-item relationships using neural networks.
- It provides an alternative to traditional collaborative filtering approaches.
- More complex models should be evaluated against simpler baselines.

### Relevance to EduTrack LMS

This paper provides a possible direction for future experimentation. The initial implementation will prioritize a reliable baseline and a matrix-factorization approach before considering a neural model.

## 5. Implementation Reference: Surprise

**Project:** Surprise — A Python scikit for recommender systems  
**Repository:** https://github.com/NicolasHug/Surprise

### Relevance to EduTrack LMS

Surprise provides recommendation algorithms, including SVD-based matrix factorization, and tools for evaluating explicit-rating recommendation systems.

Before adopting it, we will inspect the supplied datasets. If the data contains implicit engagement events rather than explicit ratings, we will select an approach appropriate for that feedback type instead of forcing the data into an unsuitable format.

## 6. Initial Design Decisions

1. Inspect and validate all supplied datasets before selecting the final model.
2. Build a baseline before tuning the primary recommendation model.
3. Compare model configurations using a consistent held-out evaluation strategy.
4. Use NDCG@10 as the primary ranking metric, with a target of at least 0.55.
5. Develop a content-based fallback for students or courses with insufficient interaction history.
6. Track experiments and document the evidence supporting model selection.
7. Measure application latency and test the serving layer before final delivery.

## 7. Conclusion

The reviewed research supports evaluating collaborative filtering and matrix factorization for personalized course recommendations. The final implementation will be guided by the actual dataset schema, measured performance, cold-start requirements, and the project's acceptance criteria.

The research establishes an initial direction; it does not represent completed model training or achieved evaluation results.
