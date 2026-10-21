import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../data/bright_light_data_clean.csv")

# Change scores (post minus baseline)
data["hippo_change"] = data["Hippocampal_volume_post"] - data["Hippocampal_volume_baseline"]
data["amyg_change"] = data["Amygdala_volume_post"] - data["Amygdala_volume_baseline"]

# Shapiro Wilk tests
print("Hippocampus:", stats.shapiro(data["hippo_change"]))
print("Amygdala:", stats.shapiro(data["amyg_change"]))

# Plots: histogram with normal curve
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

for ax, (col, title) in zip(axes, [("hippo_change", "Hippocampus"), ("amyg_change", "Amygdala")]):
    sns.histplot(data[col], stat="density", bins=15, ax=ax)
    x = np.linspace(data[col].min(), data[col].max(), 200)
    ax.plot(x, stats.norm.pdf(x, data[col].mean(), data[col].std()), color="red")
    ax.set_title(f"{title} change")

plt.tight_layout()
plt.savefig("../figures/normality_check.png")
plt.show()