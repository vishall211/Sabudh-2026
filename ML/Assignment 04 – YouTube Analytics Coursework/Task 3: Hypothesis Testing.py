import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
data = pd.read_csv("/Users/vishalsingh/Desktop/SABUDH - 26/ML/Assignment 04 – YouTube Analytics Coursework/USvideos.csv")

# Create groups based on median
likes_high = data[data["likes"] > data["likes"].median()]["views"]
likes_low = data[data["likes"] <= data["likes"].median()]["views"]

dislikes_high = data[data["dislikes"] > data["dislikes"].median()]["views"]
dislikes_low = data[data["dislikes"] <= data["dislikes"].median()]["views"]

comments_high = data[data["comment_count"] > data["comment_count"].median()]["views"]
comments_low = data[data["comment_count"] <= data["comment_count"].median()]["views"]

# Perform t-tests
likes_test = ttest_ind(likes_high, likes_low)
dislikes_test = ttest_ind(dislikes_high, dislikes_low)
comments_test = ttest_ind(comments_high, comments_low)

print("\nLikes p-value : ", likes_test.pvalue)
print("Dislikes p-value : ", dislikes_test.pvalue)
print("Comment Count p-value : ", comments_test.pvalue,"\n")

# Observation found: Likes, dislikes, and comment counts have statistically significant differences in views between 
# their high and low groups. Therefore, the hypothesis is supported.