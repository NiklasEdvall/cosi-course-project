# Clean the fictional dataset
# The original dataset is not overwritten.

import pandas as pd

# Load the original dataset. N.B: folder paths that you are in.
data = pd.read_csv("../data/bright_light_data.csv")

# I tried to change the row number column so that it starts at 1-80 instead of 0-79, doing 'data.index = range(1, len(data) + 1)' but it did not work 
# because I think positron just has the built in rows starting from 0 in their .csv files.

# Rename participant IDs to a BIDS-style format
data["Participant_id"] = data["Participant_id"].apply(
    lambda x: "sub-" + str(x).replace("P", "").zfill(3)
)

# Standardise sex labels, so that all are capitalized 
data["Sex"] = data["Sex"].str.capitalize()

# Flag the unrealistic hippocampal measurement
data.loc[
    data["Hippocampal_volume_post"] > 10,
    "Hippocampal_volume_post"
] = pd.NA

# Check the missing values
print("Missing values:")
print(data.isna().sum())

# Check which groups have participants with missing values
missing_subjects = data[data.isna().any(axis=1)]
print("\nMissing participants by group:")
print(missing_subjects["Group"].value_counts())

# Remove participants with missing values
data = data.dropna()

# Check how many participants remain in each group
print("\nRemaining participants by group:")
print(data["Group"].value_counts())

# Save the cleaned dataset separately. N.B: folder paths that you are in.
data.to_csv("../data/bright_light_data_clean.csv", index=False, na_rep="NA")

print("Cleaned dataset saved successfully!")