# %% [markdown]
# # Calculate RMSSD for each stimuli

# %%
import json
from pathlib import Path
import numpy as np
import pandas as pd

def rmssd_from_rr(rr_ms: pd.Series) -> float:
    rr = rr_ms.dropna().values.astype(float)
    if len(rr) < 2:
        return np.nan
    diff = np.diff(rr)
    return np.sqrt(np.mean(diff**2))

def load_rmssd_df(json_path: str = "experiment_with_heart_rate.json"):
    """
    Loads experiment JSON (relative to this file), computes RMSSD per video stimulus,
    and returns rmssd_df (long) and mean_table (participant-level pivot).
    """
    base = Path(__file__).resolve().parent
    jf = base / json_path

    with jf.open("r", encoding="utf-8") as f:
        participants = json.load(f)

    rows = []
    for p in participants:
        pid = p["participant_id"]
        for stim in p.get("stimuli", []):
            vid_id = stim.get("video_id")
            stim_id = stim.get("id")
            hr_rows = stim.get("heart_rate", []) or []
            if not hr_rows:
                rmssd_ms = np.nan
            else:
                df_hr = pd.DataFrame(hr_rows)
                if "ArtifactCorrectedRR" not in df_hr.columns or "ts" not in df_hr.columns:
                    rmssd_ms = np.nan
                else:
                    df_hr["ts"] = pd.to_datetime(df_hr["ts"], errors="coerce")
                    df_hr = df_hr.dropna(subset=["ts", "ArtifactCorrectedRR"]).sort_values("ts")
                    rmssd_ms = rmssd_from_rr(df_hr["ArtifactCorrectedRR"])
            belief = (stim.get("video_response", {}) or {}).get("belief")
            rows.append({
                "participant_id": pid,
                "stim_id": stim_id,
                "video_id": vid_id,
                "belief": belief,
                "RMSSD_ms": rmssd_ms,
                "RMSSD_seconds": rmssd_ms / 1000.0 if pd.notna(rmssd_ms) else np.nan,
            })

    rmssd_df = pd.DataFrame(rows)
    # standardize belief strings
    if "belief" in rmssd_df.columns:
        rmssd_df["belief"] = rmssd_df["belief"].astype(str).str.strip()
    mean_table = rmssd_df.pivot_table(index="participant_id", columns="belief", values="RMSSD_ms", aggfunc="mean")
    return rmssd_df, mean_table

rmssd_df, mean_table = load_rmssd_df("experiment_with_heart_rate.json")
rmssd_df.to_csv("rmssd_per_video.csv", index=False)

rmssd_df


# %% [markdown]
# # Check for normal distribution

# %% [markdown]
# ### Standardizing to remove accidental whitespace

# %%
rmssd_df["belief"] = rmssd_df["belief"].str.strip()


# %% [markdown]
# compute participant-level means

# %%
mean_table = (
    rmssd_df
    .pivot_table(
        index="participant_id",
        columns="belief",
        values="RMSSD_ms",
        aggfunc="mean"
    )
)


# %%
mean_table.head()


# %% [markdown]
# ### Compute within-subject difference

# %%
mean_table["diff"] = (
    mean_table["AI Generated"] - mean_table["Human Generated"]
)


# %%
diff_values = mean_table["diff"].dropna().values
diff_values


# %% [markdown]
# ### Plot the distribution

# %%
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.histplot(diff_values, kde=True, bins=20)
plt.title("Distribution of RMSSD Differences (AI-believed − Human-believed)")
plt.xlabel("RMSSD Difference (ms)")
plt.ylabel("Count")
plt.grid(True)
plt.show()


# %% [markdown]
# ### 4. Shapiro–Wilk Normality Test

# %%
from scipy.stats import shapiro

stat, p = shapiro(diff_values)

print(f"Shapiro-Wilk Test statistic: {stat:.4f}")
print(f"p-value: {p:.4f}")

if p > 0.05:
    print("✔ Differences appear normally distributed (fail to reject H0)")
else:
    print("✖ Differences are NOT normally distributed (reject H0)")


# %% [markdown]
# ### QQ Plot for RMSSD Differences

# %%
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
stats.probplot(diff_values, dist="norm", plot=plt)
plt.title("QQ Plot of RMSSD Differences")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.grid(True)
plt.show()


# %%
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Histogram + KDE
sns.histplot(diff_values, kde=True, ax=ax[0], bins=20)
ax[0].set_title("Histogram of RMSSD Differences")
ax[0].set_xlabel("Difference (AI-believed - Human-believed)")
ax[0].grid(True)

# QQ Plot
stats.probplot(diff_values, dist="norm", plot=ax[1])
ax[1].set_title("QQ Plot")
ax[1].grid(True)

plt.tight_layout()
plt.show()

# --- Add Wilcoxon signed-rank test on participant-level means ---
import numpy as np
from scipy.stats import wilcoxon

# use pivot result
# mean_table is created earlier in this notebook
paired = mean_table[["AI Generated", "Human Generated"]].dropna()
ai_vals = paired["AI Generated"].values
human_vals = paired["Human Generated"].values

# Wilcoxon signed-rank (two-sided)
stat, p = wilcoxon(ai_vals, human_vals, alternative="two-sided", zero_method="wilcox")
n = len(ai_vals)

# approximate effect size r from z
expected_W = n * (n + 1) / 4.0
std_W = np.sqrt(n * (n + 1) * (2 * n + 1) / 24.0)
z = (stat - expected_W) / std_W if std_W > 0 else np.nan
r = z / np.sqrt(n) if n > 0 else np.nan

print(f"n = {n}")
print(f"Wilcoxon W = {stat:.3f}, p = {p:.4f}")
print(f"approx. z = {z:.3f}, effect size r = {r:.3f}")

# also print medians and median difference for context
median_ai = np.median(ai_vals)
median_human = np.median(human_vals)
median_diff = np.median(ai_vals - human_vals)
print(f"median AI = {median_ai:.3f}, median Human = {median_human:.3f}, median(AI - Human) = {median_diff:.3f}")

# Interpretation hint:
# If p < 0.05, reject null of no median difference (two-sided).


