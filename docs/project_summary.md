# Salifort Motors Employee Turnover & Retention Strategy

## Issue / Problem

Salifort Motors is facing a critical retention challenge. Employee exits are primarily linked to burnout caused by excessive monthly hours and high project volume, while under-utilization also increases the risk of attrition. These patterns suggest turnover is not random, but tied to specific workload conditions and engagement gaps.

## Response & Methodology

The project cleaned and prepared a dataset of 14,999 employee records, removed duplicate entries, and engineered key features related to retention risk. A high-precision Random Forest classification model was then trained and evaluated to identify employees most likely to leave before resignation occurs.

## Impact & Model Performance

The model achieved strong predictive performance on the test set:

- Accuracy: 98.6%
- Precision: 99.1%
- Recall: 92.2%
- F1-Score: 95.5%

These results show the model is highly effective at identifying employees at risk of turnover while keeping false positives low.

## Key Insights

1. Workload controls: establish caps on monthly hours and review project distribution to reduce burnout.
2. Proactive check-ins: conduct regular engagement reviews for employees assigned to fewer than 3 or more than 5 projects.
3. Targeted retention action: use the model as an early-warning system for HR to identify at-risk employees and offer retention incentives before turnover occurs.

## Business Recommendation

Salifort Motors should treat employee workload management and targeted engagement as strategic retention priorities. By combining HR check-ins with predictive analytics, the company can intervene earlier, reduce turnover risk, and protect organizational performance.
