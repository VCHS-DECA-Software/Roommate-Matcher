import numpy as np
import pandas as pd
from algorithm import *
import sys

# Group size is 4
groupSize = 4

# Check if there is a CSV file with the list of students
if len(sys.argv) < 2:
    print("Please input a CSV file with the list of students.")
    sys.exit()

# Import the list of students as a Pandas dataframe
df = pd.read_csv(sys.argv[1])

# Initialize a matrix of student preferences with the default value of 0 (no preference)
studentPrefMatrix = np.zeros((df.shape[0], df.shape[0]), dtype=float)

# Setting myself (ex. "a@warriorlife.net")
me = "samuel.jebaraj@warriorlife.net"

# My preferences (ex. ["x@warriorlife.net", "y@warriorlife.net", "z@warriorlife.net"])
myPrefs = [
    "roshan.bellary@warriorlife.net",
    "max.zhuang@warriorlife.net",
    "kyle.zheng@warriorlife.net",
]

# Inputting preferences with the weight of a preference as the value of (the index of student i, the index of myself)
for student in myPrefs:
    studentPrefMatrix.itemset(
        (df[df["Username"] == student].index[0], df[df["Username"] == me].index[0]),
        (10 - (myPrefs.index(student) * 3)),
    )

# Saving the preference matrix
np.savetxt("Data.csv", studentPrefMatrix, delimiter=",", fmt="%d")

# Running Irving's algorithm
matching = Matching(
    studentPrefMatrix, group_size=groupSize, iter_count=2, final_iter_count=2
)
score, studentIdxs = matching.solve()
print(score)

# Converting list of student indexes to list of student names
studentGroups = []
for group in studentIdxs:
    studentGroup = []
    for studentIdx in group:
        studentGroup.append(
            "%s %s"
            % (
                df.iloc[studentIdx]["Student First Name"],
                df.iloc[studentIdx]["Student Last Name"],
            )
        )
    studentGroups.append(studentGroup)

print(studentGroups)
