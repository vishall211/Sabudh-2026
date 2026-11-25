# Task 1: Exploratory Data Analysis using Seaborn

# Import required libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
folder_path = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(folder_path, "Data set__1682565729-62fcaa4ea2bc0b6439d2306a.csv"))

# Set the style of graphs
sns.set_style("whitegrid")

# Display basic information
print("\nInput:", data.shape)
print("Output:", "Dataset loaded successfully", "\n")

# Display first five rows
print("First five rows:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(data.duplicated().sum())

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Convert FPL selection percentage into numeric format
data["fpl_sel"] = data["fpl_sel"].str.replace("%", "", regex=False)
data["fpl_sel"] = pd.to_numeric(data["fpl_sel"])

# ------------------------------------------------
# 1. Distribution of Market Value
# ------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(data=data, x="market_value", bins=30, kde=True)

plt.title("Distribution of Player Market Value")
plt.xlabel("Market Value")
plt.ylabel("Number of Players")

plt.show()

# ------------------------------------------------
# 2. Distribution of Player Age
# ------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(data=data, x="age", bins=20, kde=True)

plt.title("Distribution of Player Age")
plt.xlabel("Age")
plt.ylabel("Number of Players")

plt.show()

# ------------------------------------------------
# 3. Number of Players in Each Position
# ------------------------------------------------

plt.figure(figsize=(10, 5))

sns.countplot(data=data, x="position")

plt.title("Number of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")

plt.xticks(rotation=45)

plt.show()

# ------------------------------------------------
# 4. Market Value by Player Position
# ------------------------------------------------

plt.figure(figsize=(12, 6))

sns.boxplot(data=data, x="position", y="market_value")

plt.title("Market Value by Player Position")
plt.xlabel("Position")
plt.ylabel("Market Value")

plt.xticks(rotation=45)

plt.show()

# ------------------------------------------------
# 5. Market Value vs Age
# ------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="age",
    y="market_value"
)

plt.title("Market Value vs Player Age")
plt.xlabel("Age")
plt.ylabel("Market Value")

plt.show()

# ------------------------------------------------
# 6. Market Value vs Page Views
# ------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="page_views",
    y="market_value"
)

plt.title("Market Value vs Wikipedia Page Views")
plt.xlabel("Page Views")
plt.ylabel("Market Value")

plt.show()

# ------------------------------------------------
# 7. Market Value vs FPL Value
# ------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="fpl_value",
    y="market_value"
)

plt.title("Market Value vs FPL Value")
plt.xlabel("FPL Value")
plt.ylabel("Market Value")

plt.show()

# ------------------------------------------------
# 8. Market Value by Big Club
# ------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=data,
    x="big_club",
    y="market_value"
)

plt.title("Market Value: Big Clubs vs Other Clubs")
plt.xlabel("Big Club (0 = No, 1 = Yes)")
plt.ylabel("Market Value")

plt.show()

# ------------------------------------------------
# 9. Correlation Heatmap
# ------------------------------------------------

numeric_data = data.select_dtypes(include=["number"])

plt.figure(figsize=(12, 8))

correlation = numeric_data.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()

# ------------------------------------------------
# 10. Average Market Value by Position
# ------------------------------------------------

position_value = data.groupby("position")["market_value"].mean()

position_value = position_value.sort_values(ascending=False)

print("\nAverage Market Value by Position:")
print(position_value)

# ------------------------------------------------
# 11. Correlation with Market Value
# ------------------------------------------------

market_correlation = correlation["market_value"].sort_values(
    ascending=False
)

print("\nCorrelation with Market Value:")
print(market_correlation)

# ------------------------------------------------
# 12. Final Findings
# ------------------------------------------------

print("\nEDA Findings:")

print("1. Total number of players:", len(data))

print("2. Average market value:",
      round(data["market_value"].mean(), 2))

print("3. Highest market value:",
      data["market_value"].max())

print("4. Lowest market value:",
      data["market_value"].min())

print("5. Average age:",
      round(data["age"].mean(), 2))

print("6. Average market value of big clubs:",
      round(data[data["big_club"] == 1]["market_value"].mean(), 2))

print("7. Average market value of other clubs:",
      round(data[data["big_club"] == 0]["market_value"].mean(), 2))

print("\nInput:", data.shape)
print("Output:", "Exploratory Data Analysis completed successfully", "\n")
