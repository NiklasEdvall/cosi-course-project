## This script seperates datasets into control and light group, so that we have them seperate.
## It also seperates them.

# Library needed
import pandas as pd

# Load the cleaned dataset. N.B: folder paths that you are in.
data = pd.read_csv("../data/bright_light_data_clean.csv")

# Choose only participants in the control group
control_data = data[data["Group"] == "Control_group"]

# Choose only participants in the light group
light_data = data[data["Group"] == "Light_group"]

# Check that it worked and show exact number of participants in each group
print("Control group:", len(control_data), "participants")
print("Light group:", len(light_data), "participants")

# Ordering participants
control_data = control_data.sort_values("Participant_id")
light_data = light_data.sort_values("Participant_id")

# Save the two datasets as separate CSV files. N.B. file paths that you are in.
control_data.to_csv("../data/control_group.csv", index=False, na_rep="NA")
light_data.to_csv("../data/light_group.csv", index=False, na_rep="NA")