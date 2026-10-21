# Analyse the relationship between hippocampal and amygdala volume change

import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# Load the cleaned dataset
data = pd.read_csv("../data/bright_light_data_clean.csv")

# Calculate volume change for each brain region
data["Hippocampal_change"] = (
    data["Hippocampal_volume_post"]
    - data["Hippocampal_volume_baseline"]
)

data["Amygdala_change"] = (
    data["Amygdala_volume_post"]
    - data["Amygdala_volume_baseline"]
)

# Calculate the correlation
correlation, p_value = pearsonr(
    data["Hippocampal_change"],
    data["Amygdala_change"]
)

# Print the results
print("Correlation between volume changes")
print("Correlation coefficient:", correlation)
print("P-value:", p_value)

# Create a scatter plot using the original group colours
for group, color in [
    ("Control_group", "#ec3862"),
    ("Light_group", "#fae187")
]:
    # Select participants from this group
    group_data = data[data["Group"] == group]

    # Plot the volume changes
    plt.scatter(
        group_data["Hippocampal_change"],
        group_data["Amygdala_change"],
        label=group,
        color=color,
        alpha=0.7
    )

# Add labels and a legend
plt.xlabel("Hippocampal volume change")
plt.ylabel("Amygdala volume change")
plt.title("Brain volume changes by group")
plt.axhline(0, color="grey", linestyle="--", linewidth=0.8)
plt.axvline(0, color="grey", linestyle="--", linewidth=0.8)
plt.legend()

# Save and display the figure
plt.tight_layout()
plt.savefig("../figures/brain_volume_correlation_by_group.png", dpi=300)
plt.show()