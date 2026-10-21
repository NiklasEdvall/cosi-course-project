# T tests for the bright light therapy study
#
# Research question: was bright light therapy associated with a different
# change in brain volume over eight weeks than the control condition?
#
# For the hippocampus and the amygdala, two tests are run:
#   1. Paired t test: did volume change from baseline to week 8 at all?
#      (all participants together, so this does not tell us about the therapy)
#   2. Welch independent t test: did the control group and the bright light
#      group change by different amounts?

import pandas as pd
from scipy.stats import ttest_rel, ttest_ind

data = pd.read_csv("../data/bright_light_data_clean.csv")

# Forloop, for running the same two tests for each brain region (hippocampus and amygdala). Forloop was written with help of Claude.ai because 
# my script for writing everything out in itself got too long. I compared scripts though and got the same results.
for region in ["Hippocampal", "Amygdala"]:
    baseline = data[f"{region}_volume_baseline"]
    post = data[f"{region}_volume_post"]
    change = post - baseline

    # Change scores for each group
    control = change[data["Group"] == "Control_group"]
    light = change[data["Group"] == "Light_group"]

    # Paired t test: did volume change from baseline to post (all participants, but paired because comparing values of same participant - within)?
    paired = ttest_rel(post, baseline)

    # Welch t test: did the two groups change by different amounts?
    groups = ttest_ind(control, light, equal_var=False)

    print(f"\n{region}")
    print("Mean change, control:", round(control.mean(), 3))
    print("Mean change, bright light:", round(light.mean(), 3))
    print("Paired t test p value:", round(paired.pvalue, 3))
    print("Group comparison p value:", round(groups.pvalue, 3))

## Results

# Hippocampal
# Mean change, control: 0.03 
# Mean change, bright light: 0.05 
# Paired t test p value: 0.001 --> Volume increased over eight weeks in all participants
# Group comparison p value: 0.374 --> The groups did not differ significantly in their change in brain volume.

# Amygdala
# Mean change, control: 0.021
# Mean change, bright light: 0.041
# Paired t test p value: 0.0 --> Volume increased over eight weeks in all participants 
# Group comparison p value: 0.203 --> The groups did not differ significantly in their change in brain volume.

# => No evidence that bright light led to a larger increase.

# OVERALL

# Both regions grew in everyone.
# Neither region grew significantly more with bright light.
# A p value above 0.05 means no evidence of a difference, not proof that there is none.