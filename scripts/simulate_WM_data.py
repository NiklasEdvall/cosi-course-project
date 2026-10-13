# This project creates a fictional dataset for Python practice. It explores a hypothetical relationship between bright light
# therapy and changes in brain volume over 8 weeks.
# N.B.: The participants and measurements are fictional. The results do NOT represent real scientific findings. 
# CHATGPT was used as help in the creation of this code.

# Import python libraries

import numpy as np # helps us create random numbers. we will use it to generate ages and brain volume measurements
import pandas as pd # to create and save our dataset (organises information into a table)

# Set the output folder and filename. Make sure to be in the right directory.
output_folder = "data"
output_filename = "bright_light_data.csv"

# Make the results reproducible. 
np.random.seed(42) # it makes sure we get same random results every time the script is run.

# Total number of participants
n = 80

# Create participant IDs
participant_id = []

## This code creates a unique ID for each participant
for i in range(1, n + 1):
    participant_id.append("P" + str(i).zfill(3))

# Create two groups: 40 participants in each
group = ["light_group"] * 40 + ["control_group"] * 40

# Shuffle the group order
np.random.shuffle(group)

# Create demographic variables that are random. 
age = np.random.randint(18, 41, n) # 18 is minimum, 41 is maximum age

sex = np.random.choice(["Female", "Male"], n) # assign randomly female or male

country = np.random.choice(["Sweden", "Australia"], n) # participants are either from Sweden or from Australia, also assigned randomly

# Create hippocampal volume measurements.
# These are fictional volume measurements in cubic centimetres.
hippo_baseline = np.random.normal(7.0, 0.7, n) # np.random.normal creates random numbers around an average. Here, the average is 7.0 and the spread is 0.7.

# Create an empty list for the measurements after 8 weeks.
hippo_post = []

# Go through the participants one at a time.
for i in range(n):

    # Check which group the participant belongs to.
    if group[i] == "light_group":
        change = np.random.normal(0.05, 0.10) # gives the light group a small hypothetical average change.The change is random for each participant.
    else:
        change = np.random.normal(0.00, 0.10) # gives the control group a different hypothetical change.

    # Calculate the 8-week measurement.
    hippo_post.append(hippo_baseline[i] + change) # new measurement = baseline measurement + change.

# Create amygdala volume measurements. 
# These are also fictional measurements in cubic centimetres.
amygdala_baseline = np.random.normal(3.5, 0.4, n) # The average is set to 3.5, with a spread of 0.4.

# Create an empty list for the 8-week measurements.
amygdala_post = []

# Go through the participants one at a time.
for i in range(n):

    # Check whether the participant is in the light group.
    if group[i] == "light_group":
        change = np.random.normal(0.03, 0.06) #  adds a small hypothetical average change.
    else:
        change = np.random.normal(0.00, 0.06) #  use a different average change for the control group.

    # Calculate the 8-week measurement.
    amygdala_post.append(amygdala_baseline[i] + change)

# Putting everything in one table. A pandas DataFrame is a table with rows and columns.
# Each row will represent one participant.
# Each column will contain one type of information.
data = pd.DataFrame({

    # Participant information
    "participant_id": participant_id,
    "group": group,
    "age": age,
    "sex": sex,
    "country": country,

    # Hippocampal measurements
    # Round the measurements to 2 decimal places.
    "hippocampal_volume_baseline": np.round(hippo_baseline, 2),
    "hippocampal_volume_post": np.round(hippo_post, 2),

    # Amygdala measurements
    "amygdala_volume_baseline": np.round(amygdala_baseline, 2),
    "amygdala_volume_post": np.round(amygdala_post, 2)
})

# Missing values are useful for practising data cleaning. np.nan represents a missing numerical value.
# These lines remove three measurements from the dataset.

data.loc[2, "hippocampal_volume_post"] = np.nan
data.loc[10, "hippocampal_volume_post"] = np.nan
data.loc[20, "hippocampal_volume_post"] = np.nan

# Most labels use a capital letter, such as "Female". Change two labels to lowercase to create inconsistencies.
# This gives us something to fix during data cleaning.

data.loc[3, "sex"] = "female"
data.loc[15, "sex"] = "male"

# Set one hippocampal measurement to 70.0. This is an intentionally unrealistic value for this dataset.
# It lets us practise finding unusual values during data cleaning.

data.loc[25, "hippocampal_volume_post"] = 70.0

# Mix the rows so the participants are not in their original order. random_state=42 makes this shuffle repeatable.
data = data.sample(frac=1, random_state=42).reset_index(drop=True) # reset_index(drop=True) gives the rows new index numbers.

# Save the table as a CSV file.
data.to_csv(output_folder + "/" + output_filename, index=False) # index=False means we do not save an extra index column.

print(data.head()) #prints the first five rows of the dataset.
print(data["group"].value_counts()) # shows how many participants are in each group.
print("Dataset dimensions:", data.shape) # shows the number of rows and columns. Expected result: 80 rows and 9 columns.
print("CSV file created successfully!") # prints a final message to confirm the script has run.