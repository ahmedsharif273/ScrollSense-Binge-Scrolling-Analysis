# ScrollSense: Binge-Scrolling & Academic Impact Analysis

A behavioral analytics study on compulsive social media scrolling among university students, and how strongly it links to academic performance.

**[Live Dashboard](https://ahmedsharif273.github.io/ScrollSense-Binge-Scrolling-Analysis/binge_scrolling_dashboard.html)** · **[Analysis Notebook](analysis_notebook.ipynb)**

---

## Overview

This project analyzes survey data from **150 university students**, covering demographics, social media usage habits, and 24 Likert-scale (1–5) items measuring compulsive scrolling behavior and its effect on academic life. The goal was to answer three questions:

1. Is "binge-scrolling" a measurable, reliable construct — not just anecdote?
2. Does it actually correlate with academic disruption (procrastination, lost focus, anxiety)?
3. Can students be segmented into meaningful behavioral groups?

## Key Findings

| Metric | Result |
|---|---|
| Binge-Scrolling Index reliability | Cronbach's α = 0.885 |
| Academic Impact Index reliability | Cronbach's α = 0.814 |
| Correlation (scrolling ↔ academic impact) | r = 0.78, p < .001 |
| Significant group differences | Academic year (p < .001), Gender (p = .003) |
| Behavioral personas identified | Low-Risk (21%), Moderate (35%), At-Risk (44%) |

**Takeaway:** Binge-scrolling isn't just loosely associated with academic strain — it's one of the more consistent behavioral predictors in this sample, with nearly half of students falling into an "at-risk" pattern where compulsive use tracks closely with procrastination and lost study focus.

## Methodology

1. **Composite index construction** — averaged 12 items into a Binge-Scrolling Index and 4 items into an Academic Impact Index
2. **Reliability testing** — Cronbach's alpha to confirm both scales are internally consistent before treating them as single scores
3. **Correlation analysis** — Pearson correlation between the two indices
4. **Group comparisons** — one-way ANOVA and t-tests across academic year, gender, field of study, platform, and daily usage hours
5. **Clustering** — K-means (k=3, standardized inputs) on all 16 Likert items to segment students into behavioral personas

## Repository Contents

| File | Description |
|---|---|
| `analysis_notebook.ipynb` | Full analysis pipeline with explanations and charts — run directly in Google Colab |
| `analysis.py` | Same analysis as a clean, reproducible Python script |
| `binge_scrolling_dashboard.html` | Interactive dashboard with filterable charts (open directly in a browser) |
| `Cleaned_Thesis_Data.csv` | Source survey dataset (150 responses, 25 columns) |
| `processed_data.csv` | Output data with composite indices, cluster labels, and personas attached |

## Running This Yourself

**Notebook (Colab):**
Open `analysis_notebook.ipynb` in Google Colab, upload `Cleaned_Thesis_Data.csv` when prompted, and run all cells.

**Script (local):**
```bash
pip install pandas numpy scipy scikit-learn
python analysis.py
```

**Dashboard:**
Just open `binge_scrolling_dashboard.html` in any browser — no server needed.

## Tools Used

Python (pandas, scipy, scikit-learn, matplotlib, seaborn) · Chart.js · HTML/CSS/JS

---

*Part of a broader interest in applying data science to digital wellbeing and student behavior research.*
"# ScrollSense-Binge-Scrolling-Analysis" 
