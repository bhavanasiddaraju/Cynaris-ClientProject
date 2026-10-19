# A/B Testing Plan — EduTrack LMS

## 1. Purpose

This document describes a proposed A/B test for evaluating whether the EduTrack LMS recommendation system improves student engagement compared with a baseline recommendation strategy.

The experiment will be conducted only after the recommendation system is implemented and an appropriate testing environment and participant permissions are available.

## 2. Experiment Objective

Compare a candidate personalized recommendation system with a baseline strategy to determine whether personalized course recommendations improve course engagement without reducing recommendation quality or creating unacceptable disparities between student groups.

## 3. Experimental Variants

### Control Group — A

Students receive recommendations from the baseline strategy, such as courses ranked by historical popularity, subject to course eligibility and available data.

### Treatment Group — B

Students receive personalized recommendations from the selected collaborative-filtering model, with the documented fallback for students who lack sufficient interaction history.

Both groups should use the same eligible course catalogue and comparable presentation formats so that the recommendation strategy is the principal difference.

## 4. Assignment Method

Eligible participants will be randomly assigned to Group A or Group B.

Where feasible, assignment will remain stable for each participant throughout the experiment to reduce contamination between variants.

The experiment should define eligibility rules before assignment. Any required consent, institutional approval, privacy review, and data-protection measures must be completed before a live student experiment begins.

## 5. Primary Outcome

The proposed primary outcome is the course engagement rate.

The exact definition will be fixed before the experiment. One possible definition is:

**Course engagement rate = Number of recommended-course impressions followed by a defined engagement action / Total eligible recommended-course impressions**

The engagement action might be a course click or course start, depending on which events are reliably recorded in the platform.

The chosen denominator, attribution window, and qualifying event will be documented before data collection.

## 6. Secondary Outcomes

The experiment may also measure:

- Course-start rate.
- Course-completion rate, if completion data is available.
- Number of distinct courses engaged with.
- Student return or continued-learning rate.
- NDCG@10 or another suitable offline ranking metric.
- Latency and recommendation failure rate.

Offline ranking metrics and live engagement outcomes will be reported separately because they measure different aspects of performance.

## 7. Sample Size and Duration

The required sample size will be estimated before launch using a baseline engagement rate, a predefined minimum detectable effect, a significance level, and a desired statistical power.

The experiment duration will account for sufficient participation and relevant learning activity patterns.

No sample size, duration, or statistical result will be claimed until these values are established.

## 8. Analysis Plan

Before starting the experiment:

1. Define the primary outcome and analysis window.
2. Establish eligibility and exclusion criteria.
3. Choose the statistical test appropriate for the outcome and randomization unit.
4. Set a significance level, such as 0.05, and a target statistical power, such as 80%.
5. Specify how missing data, repeated observations, and multiple comparisons will be handled.
6. Document the analysis plan before inspecting outcome differences.

After the experiment, report outcome rates for both groups, the estimated difference, an appropriate confidence interval, and the statistical test result.

A statistically significant difference will not automatically be interpreted as practically meaningful.

## 9. Guardrails and Fairness

Monitor:

- API errors and response latency.
- Empty or duplicate recommendations.
- Course availability and eligibility.
- Differences in engagement across relevant student groups where data collection and privacy rules permit.
- Potential disadvantages for new students with limited interaction history.

Do not use sensitive personal attributes to personalize recommendations without explicit authorization, a legitimate basis, and appropriate safeguards.

## 10. Decision Criteria

The treatment strategy may be considered for adoption if it:

- Shows a meaningful improvement in the predefined primary outcome.
- Does not violate agreed performance or reliability guardrails.
- Provides an acceptable experience for students with little or no history.
- Has no unresolved fairness, privacy, or operational concerns.

If the evidence is inconclusive, retain the baseline while gathering additional evidence or revising the experiment design.

## 11. Risks and Limitations

- Small samples may not detect meaningful differences.
- Course popularity and student characteristics can influence observed engagement.
- Students may engage with recommendations outside the defined attribution window.
- Offline ranking improvements may not translate directly into higher completion rates.
- Changes to course availability during the experiment may affect results.

These risks will be considered when interpreting findings.

## 12. Current Status

This document describes a proposed A/B testing design. No live experiment has been conducted and no treatment effect has been measured.
