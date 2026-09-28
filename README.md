# Customer Churn Analysis — Python / pandas

Exploratory customer-retention analysis using a synthetic telecom-style dataset.

## Dataset
- 7,043 customer records
- 13 fields covering tenure, contract, service, billing and churn
- Synthetic data created specifically for this portfolio

## Questions explored
- What is the overall churn rate?
- How does contract type relate to churn?
- Which payment methods show higher churn?
- Does tech support correlate with retention?
- How do monthly charges differ between churned and retained customers?

## Selected findings
- Overall churn rate: **25.3%**
- Month-to-month churn: **39.1%**
- One-year contract churn: **9.7%**
- Two-year contract churn: **7.0%**
- Highest-churn payment method: **Electronic check** (31.0%)

## Skills demonstrated
Python, pandas, data cleaning, segmentation, descriptive analysis, KPI calculation and Matplotlib visualization.

## Run
```bash
pip install -r requirements.txt
python generate_data.py
python analysis.py
```

Outputs are saved to `outputs/`.

> The dataset is synthetic. Findings demonstrate analytical workflow, not claims about a real telecom company.