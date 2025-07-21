# HealthKart Influencer Campaign Dashboard

This project provides a complete data-driven system to analyze influencer marketing performance for HealthKart campaigns across various platforms and products.

---

## Task Overview

HealthKart runs influencer campaigns on platforms like Instagram, YouTube, and Twitter to promote products under brands like MuscleBlaze, HKVitals, and Gritzo.

### Objective:
Build an interactive dashboard that can:
- Track campaign and post performance
- Calculate ROAS (Return on Ad Spend) and Incremental ROAS
- Provide insights into top and poor-performing influencers
- Monitor influencer payouts
- Support brand-level, platform-level, and persona-level analysis

---

## What the Project is Based On

This project uses:
- Python for data simulation and analysis
- Streamlit for an interactive dashboard
- Pandas and NumPy for data wrangling
- Faker for synthetic data generation
- Modular design with structured folders for simulation, modeling, analysis, and visualization

---

## File Breakdown

```
healthkart-influencer-dashboard/
│
├── data/                         # Auto-generated CSVs
│   ├── influencers.csv
│   ├── posts.csv
│   ├── tracking_data.csv
│   ├── payouts.csv
│   ├── performance_summary.csv
│   ├── roas_summary.csv
│   └── city_roas.csv, poor_influencers.csv
│
├── modeling/
│   └── data_modeling.py          # Documents all data schemas used
│
├── simulation/
│   └── simulate_data.py          # Generates influencers, posts, tracking, payouts
│
├── analysis/
│   ├── performance_tracking.py   # Aggregates performance metrics
│   ├── roas_calculation.py       # Computes ROAS and incremental ROAS
│   └── filtering_insights.py     # Filters top personas and poor performers
│
├── app.py                        # Streamlit dashboard to explore all results
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## How to Run This Project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate All Datasets
```bash
python simulation/simulate_data.py
```

### Step 3: Compute Performance Metrics
```bash
python analysis/performance_tracking.py
```

### Step 4: Calculate ROAS and Incremental ROAS
```bash
python analysis/roas_calculation.py
```

### Step 5: Extract Insights (Top Personas, Cities, Low ROAS)
```bash
python analysis/filtering_insights.py
```

### Step 6: Launch the Interactive Dashboard
```bash
streamlit run app.py
```

---

## Requirements

Dependencies are listed in `requirements.txt`:

```
streamlit
pandas
numpy
faker
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Output Summary

The dashboard supports:
- Filtering by brand and platform
- Viewing average and top ROAS metrics
- Displaying top influencer table
- Viewing ROAS by persona and city
- Identifying bottom 10% influencers

All outputs are saved under the `data/` folder for further reporting or visualization.

---

## Notes

- All data is simulated and randomized
- You can expand it by adding A/B test logs, real-time ingestion, or ML-based scoring
