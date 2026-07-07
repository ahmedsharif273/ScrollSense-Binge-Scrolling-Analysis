"""
Binge-Scrolling & Academic Impact — Analysis Pipeline
------------------------------------------------------
Input:  Cleaned_Thesis_Data.xlsx  (n=150 student survey responses)
Output: processed_data.csv + printed statistical results

Sections:
 1. Composite index construction (Binge-Scrolling, Academic Impact)
 2. Reliability check (Cronbach's alpha)
 3. Correlation analysis
 4. Group comparisons (ANOVA / t-tests) across demographics & habits
 5. K-means clustering into behavioral personas
"""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr, f_oneway, ttest_ind
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

INPUT_FILE = "Cleaned_Thesis_Data.csv"

BINGE_COLS = [
    "Q13_Continuous_Scroll", "Q14_Scroll_Until_Bored", "Q15_Scroll_No_Purpose",
    "Q16_Scroll_When_Alone", "Q17_Physically_Uncomfortable", "Q18_Feel_Guilty",
    "Q19_Feel_Depressed", "Q20_Mad_At_Self", "Q21_Struggle_To_Control",
    "Q22_Thinking_About_Scrolling", "Q23_Scroll_More_Than_Planned", "Q24_Cannot_Stop_Self",
]
ACADEMIC_COLS = [
    "Q25_Procrastinate_Academic_Work", "Q26_Reduces_Study_Efficiency",
    "Q27_Lose_Study_Concentration", "Q28_Anxious_Without_Social_Media",
]


def cronbach_alpha(df_sub: pd.DataFrame) -> float:
    """Standard Cronbach's alpha for a set of Likert items."""
    df_sub = df_sub.dropna()
    item_vars = df_sub.var(axis=0, ddof=1)
    total_var = df_sub.sum(axis=1).var(ddof=1)
    n_items = df_sub.shape[1]
    return (n_items / (n_items - 1)) * (1 - item_vars.sum() / total_var)


def main():
    df = pd.read_csv(INPUT_FILE)

    # ---- 1 & 2: composite indices + reliability ----
    alpha_binge = cronbach_alpha(df[BINGE_COLS])
    alpha_academic = cronbach_alpha(df[ACADEMIC_COLS])
    print(f"Cronbach's alpha — Binge-Scrolling Index:  {alpha_binge:.3f}")
    print(f"Cronbach's alpha — Academic Impact Index:  {alpha_academic:.3f}\n")

    df["Binge_Index"] = df[BINGE_COLS].mean(axis=1)
    df["Academic_Impact_Index"] = df[ACADEMIC_COLS].mean(axis=1)

    # ---- 3: correlation ----
    r, p = pearsonr(df["Binge_Index"], df["Academic_Impact_Index"])
    print(f"Correlation (Binge Index vs Academic Impact): r={r:.3f}, p={p:.5f}\n")

    # ---- 4: group comparisons ----
    print("Group comparisons on Binge_Index (one-way ANOVA):")
    for col in ["Field_of_Study", "Age", "Academic_Year", "Binge_Scroll_Platform",
                "Peak_Usage_Time", "Daily_Hours_Spent"]:
        groups = [g["Binge_Index"].values for _, g in df.groupby(col)]
        f_stat, p_val = f_oneway(*groups)
        flag = "**" if p_val < 0.05 else ""
        print(f"  {col:25s} F={f_stat:6.2f}  p={p_val:.4f} {flag}")

    male = df.loc[df["Gender"] == "Male", "Binge_Index"]
    female = df.loc[df["Gender"] == "female", "Binge_Index"]
    t_stat, p_val = ttest_ind(male, female)
    print(f"\nGender (Male vs female) t-test: t={t_stat:.2f}, p={p_val:.4f}\n")

    # ---- 5: clustering into personas ----
    features = df[BINGE_COLS + ACADEMIC_COLS]
    X_scaled = StandardScaler().fit_transform(features)

    for k in (2, 3, 4):
        labels = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(X_scaled)
        print(f"k={k} silhouette score: {silhouette_score(X_scaled, labels):.3f}")

    km = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X_scaled)
    df["Cluster"] = km.labels_

    order = df.groupby("Cluster")["Binge_Index"].mean().sort_values().index.tolist()
    label_map = {order[0]: "Low-Risk", order[1]: "Moderate", order[2]: "At-Risk"}
    df["Persona"] = df["Cluster"].map(label_map)

    print("\nPersona breakdown:")
    print(df.groupby("Persona")[["Binge_Index", "Academic_Impact_Index"]]
            .agg(["mean", "count"]))

    df.to_csv("processed_data.csv", index=False)
    print("\nSaved processed_data.csv")


if __name__ == "__main__":
    main()
