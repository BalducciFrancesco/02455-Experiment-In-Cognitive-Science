#_rmssd_py
# %% [markdown]
# ## Helper to compute RMSSD from an RR series
# 
# RMSSD_ms: This is RMSSD expressed in milliseconds, the normal HRV unit. RMSSD_seconds is the same value but in seconds instead of ms. An RMSSD value of 34.2 ms would mean that the variability between heartbeats is about 34.2 ms.

# %%
import numpy as np
import pandas as pd
import json

def rmssd_from_rr(rr_ms: pd.Series) -> float:
    rr = rr_ms.dropna().values.astype(float)
    if len(rr) < 2:
        return np.nan
    diff = np.diff(rr)
    return np.sqrt(np.mean(diff**2))

# %% [markdown]
# ## Load merged JSON (if not already in memory)

# %%
# load merged experiment JSON
with open("experiment_with_heart_rate.json", "r", encoding="utf-8") as f:
    participants = json.load(f)

# %% [markdown]
# ## Loop: RMSSD per video per participant

# %%
rows = []

for p in participants:
    pid = p["participant_id"]

    for stim in p["stimuli"]:
        vid_id = stim["video_id"]
        stim_id = stim["id"]

        hr_rows = stim.get("heart_rate", [])
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

        # participant's belief from JSON
        belief = stim.get("video_response", {}).get("belief")

        rows.append({
            "participant_id": pid,
            "stim_id": stim_id,
            "video_id": vid_id,
            "belief": belief,
            "RMSSD_ms": rmssd_ms,
            "RMSSD_seconds": rmssd_ms / 1000.0 if pd.notna(rmssd_ms) else np.nan,
        })

rmssd_df = pd.DataFrame(rows)
rmssd_df

# %% [markdown]
# ## Save to CSV

# %%
rmssd_df.to_csv("rmssd_per_video.csv", index=False)


# %% [markdown]
# ## Labels
# 

# %%
import pandas as pd

design = pd.read_csv("variables/subjects_design.csv")
print(design.columns)

# %%
# if there is no 'subject' column, we create participant_id from row index
if "subject" in design.columns:
    design["participant_id"] = design["subject"]
else:
    design = design.reset_index(drop=True)
    design["participant_id"] = design.index + 1  # 1,2,3,...

rows = []
for _, row in design.iterrows():
    pid = row["participant_id"]
    for i in range(1, 5):  # video1..video4
        video_col = f"video{i}"
        label_col = f"label{i}"
        video = row[video_col]
        label = row[label_col]
        rows.append({
            "participant_id": pid,
            "stim_id": i,          # 1..4, matches your stim['id']
            "video_id": video,
        })

design_long = pd.DataFrame(rows)
print(design_long.head())


# %%
rmssd_labeled = rmssd_df.merge(
    design_long,
    on=["participant_id", "stim_id", "video_id"],
    how="left",
)

rmssd_labeled.head()


# %% [markdown]
# # Save to CSV

# %%
rmssd_labeled.to_csv("rmssd_per_video.csv", index=False)


# %% [markdown]
# # Check for normal distribution

# %% [markdown]
# ### Standardizing to remove accidental whitespace

# %%
rmssd_labeled["belief"] = rmssd_labeled["belief"].str.strip()


# %% [markdown]
# compute participant-level means

# %%
mean_table = (
    rmssd_labeled
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



