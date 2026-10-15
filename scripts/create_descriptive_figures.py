# Visualisation 1 - Age distribution by group - boxplot

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
data = pd.read_csv("../data/bright_light_data_clean.csv")

# Compare ages between the two groups
fig, ax = plt.subplots()

data.boxplot(
    column="Age",
    by="Group",
    ax=ax,
    patch_artist=True
)

# Colour the boxes
colors = ["#ec3862", "#fae187"]

for box, color in zip(ax.patches, colors):
    box.set_facecolor(color)

# Add titles and labels
ax.set_title("Age Distribution by Group")
fig.suptitle("")
ax.set_xlabel("Group")
ax.set_ylabel("Age (years)")

plt.tight_layout()
plt.savefig("../figures/age_distribution.png", dpi=300, bbox_inches="tight")
plt.show()



# Visualisation 2 - Sex distribution by group

# Count participants by sex and group
sex_counts = pd.crosstab(data["Sex"], data["Group"])

# Create the bar chart with pink and yellow bars
ax = sex_counts.plot(
    kind="bar",
    color=["#ec3862", "#fae187"]
)

# Add titles and labels
ax.set_title("Sex Distribution by Group")
ax.set_xlabel("Sex")
ax.set_ylabel("Number of Participants")
ax.tick_params(axis="x", rotation=0)

# Changing the legend title so that's its not in the way of the bars in the chart
ax.legend(title="Group", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig("../figures/sex_distribution.png", dpi=300, bbox_inches="tight")
plt.show()




# Visualisation 3 - Country distribution by group

# Calculate country percentages within each group
country_percent = pd.crosstab(
    data["Country"], data["Group"], normalize="columns"
) * 100

# Create a grouped bar chart
country_percent[["Control_group", "Light_group"]].plot(
    kind="bar",
    color=["#ec3862", "#fae187"]
)

plt.title("Country distribution by group")
plt.xlabel("Country")
plt.ylabel("Participants (%)")
plt.xticks(rotation=0)
plt.legend(title="Groups")
plt.tight_layout()
plt.savefig("../figures/country_distribution.png", dpi=300, bbox_inches="tight")
plt.show()