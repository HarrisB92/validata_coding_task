# Part 2 — Loan Approval Prediction (KNN vs Decision Tree)

## Overview

The objective of this task was to predict whether a loan application will be approved based on
applicant and loan characteristics. Two machine learning models were developed and evaluated:

- K-Nearest Neighbors (KNN)
- Decision Tree

The target variable is binary (`loan_approved`), indicating whether a loan was approved.

---

## Dataset Description

A synthetic dataset of 500 loan applications was generated to resemble a realistic retail banking
scenario. The dataset includes the following features:

- income
- credit_score
- loan_amount
- loan_term
- employment_status (categorical)
- loan_approved (target)

The dataset was generated using realistic statistical distributions and correlated features.
Loan approval was modeled probabilistically (not deterministically based on if rules) to reflect real-world uncertainty rather than hard
rule-based decisions.

---

## Preprocessing

Before training the models, the following preprocessing steps were applied:

- Numerical features were standardized using `StandardScaler`
- Categorical features were one-hot encoded
- The dataset was split into training (80%) and testing (20%) sets
- Class stratification was used to preserve approval rate balance

Preprocessing was applied inside the modeling pipeline to avoid data leakage.

---

## Model Evaluation

Both models were evaluated on the same test set using the following metrics:
- Accuracy
- Precision
- Recall
- F1-score

### Evaluation Results

- Model parameters were selected as reasonable defaults to balance performance, interpretability, and overfitting, as the goal was comparative evaluation rather than optimization. 

Model                          Accuracy   Precision   Recall     F1-score
KNN (k=7)                      0.75       0.80        0.75       0.77
Decision Tree (max_depth=5)    0.66       0.70        0.70       0.70

---

## Model Comparison

The KNN model outperformed the Decision Tree across all evaluation metrics, particularly in
F1-score, indicating a better balance between precision and recall.

However, the Decision Tree offers greater interpretability, which is often an important
consideration in regulated domains such as banking.

---

## Feature Importance Analysis

Feature importance was analyzed using the Decision Tree model.

Top contributing features:

1. credit_score
2. income
3. loan_amount
4. employment_status (unemployed)
5. loan_term

Credit score was by far the most influential feature, followed by income and loan amount.
Employment status and loan term also contributed, but to a lesser extent.

---

## Business Insights

Based on the analysis, the following insights can be provided to the bank:

- Credit score is the strongest indicator of loan approval and should remain a primary decision factor
- Income relative to loan amount plays a significant role in approval decisions
- Employment stability affects approval likelihood, especially for unemployed applicants
- Loan term has a smaller but non-negligible impact on approval outcomes

From a business perspective, these findings suggest that:
- Improving credit assessment processes can significantly enhance decision quality (focus on methodology, formulas and processes)
- Offering alternative products for lower-income or self-employed applicants may improve inclusion (e.g. smaller loans, shorter loan terms, different interest rates)
- Transparent, explainable models such as Decision Trees may be preferable in regulated environments,
  even if slightly less accurate than KNN

---

## Conclusion

While KNN achieved higher predictive performance, the Decision Tree model provides better
interpretability and insight into decision drivers. Depending on regulatory and business
requirements, either model could be appropriate, with Decision Trees being a strong candidate
when explainability is a priority.
