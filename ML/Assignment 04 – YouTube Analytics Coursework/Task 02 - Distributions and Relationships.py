import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
csv_path = os.path.join(os.path.dirname(__file__), "USvideos.csv")
data = pd.read_csv(csv_path)

# Create title length
data["title_length"] = data["title"].str.len()

# Histogram of views
plt.hist(data["views"])
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.title("Distribution of Views")
plt.show()

# Scatterplot: Likes vs Views
plt.scatter(data["likes"], data["views"])
plt.xlabel("Likes")
plt.ylabel("Views")
plt.title("Likes vs the Views")
plt.show()

# Correlation matrix
features = ["views","likes","dislikes","comment_count","title_length"]
print("\nCorrelation Matrix : ", data[features].corr(),"\n")

#  Observation Noticed: 
# 1. Likes have a strong positive correlation with views. 
# 2. Comment count and dislikes show moderate positive correlations with views, 
# 3. while title length has almost no correlation with views.