import os
import pandas as pd
import numpy as np

csv_path = os.path.join(os.path.dirname(__file__), "USvideos.csv")
data = pd.read_csv(csv_path)

print("\nDataset Shape : ", data.shape)     # Dataset shape

print("\nTop 5 rows : \n",data.head())               # Display top 5 rows
print("\nDataset Information : \n",data.info())      # Display dataset infromation
print("\nDataset Summary : \n",data.describe())      # Display statistical summary

# Find the top 25% views threshold
print("\n")
viral_threshold = data["views"].quantile(0.75)

# Create / Display viral column
print("\n")
data["viral"] = (data["views"] > viral_threshold).astype(int)
print(data[["views", "viral"]].head(10))

# Display number of viral and non-viral videos
print("\n")
print(data["viral"].value_counts(),"\n")