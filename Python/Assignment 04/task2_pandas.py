import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Answer 01 : Load dataset and display first 5 rows
def load_data():
    data = pd.read_csv("Python/Assignment 04/1_Sport car price.csv")
    return data


# Answer 02 : Clean the dataset
def clean_data(data):
    # data = data.drop_duplicates()     It is showing warnings
    data = data.drop_duplicates().copy()

    data["Engine Size (L)"] = pd.to_numeric(data["Engine Size (L)"], errors="coerce")
    data["Horsepower"] = pd.to_numeric(data["Horsepower"], errors="coerce")
    data["Torque (lb-ft)"] = pd.to_numeric(data["Torque (lb-ft)"], errors="coerce")
    data["0-60 MPH Time (seconds)"] = pd.to_numeric(data["0-60 MPH Time (seconds)"], errors="coerce")

    data["Price (in USD)"] = data["Price (in USD)"].str.replace(",", "")
    data["Price (in USD)"] = pd.to_numeric(data["Price (in USD)"], errors="coerce")

    data = data.dropna()
    return data


# Answer 03 : Summary statistics
def summary_stats(data):
    num_data = data.select_dtypes(include="number")

    stats = pd.DataFrame({
        "Mean": num_data.mean(),
        "Median": num_data.median(),
        "Mode": num_data.mode().iloc[0],
        "Standard Deviation": num_data.std(),
        "Range": num_data.max() - num_data.min()
    })
    return stats


# Answer 04 : Average price by car make
def price_by_make(data):
    result = data.groupby("Car Make")["Price (in USD)"].mean()
    return result


# Answer 05 : Average horsepower by year
def horsepower_by_year(data):
    result = data.groupby("Year")["Horsepower"].mean()
    return result


# Answer 06 : Price vs horsepower with regression line
def price_horsepower_plot(data):
    horsepower = data["Horsepower"]
    price = data["Price (in USD)"]
    line = np.polyfit(horsepower, price, 1)
    model = np.poly1d(line)

    plt.scatter(horsepower, price)
    plt.plot(horsepower, model(horsepower))
    plt.xlabel("Horsepower")
    plt.ylabel("Price")
    plt.title("Price vs Horsepower")

    plt.show()


# Answer 07 : Histogram of 0-60 MPH times
def mph_histogram(data):
    start = data["0-60 MPH Time (seconds)"].min()
    end = data["0-60 MPH Time (seconds)"].max()
    bins = np.arange(start, end + 0.5, 0.5)

    plt.hist(data["0-60 MPH Time (seconds)"], bins=bins)

    plt.xlabel("0-60 MPH (Time in seconds)")
    plt.ylabel("Number of Cars")
    plt.title("0-60 MPH Times")
    plt.show()


# Answer 08 : Cars with price greater than $500,000
def expensive_cars(data):
    result = data[data["Price (in USD)"] > 500000]
    result = result.sort_values("Horsepower", ascending=False)

    return result


# Answer 09 : Export cleaned dataset
def export_data(data):
    data.to_csv("Python/Assignment 04/2_cleaned_sports_cars.csv", index=False)


if __name__ == "__main__":

# --------------------------------------------------------------------------|
    data = load_data()

    print("------------ Answer 01 ------------\n")
    print(data.head(5))

# --------------------------------------------------------------------------|
    data = clean_data(data)

    print("\n\n------------ Answer 02 ------------")
    print("\nCleaned data:")
    print(data.head())

# --------------------------------------------------------------------------|
    stats = summary_stats(data)

    print("\n\n------------ Answer 03 ------------")
    print("\nSummary Statistics:")
    print(stats)

# --------------------------------------------------------------------------|
    make_price = price_by_make(data)

    print("\n\n------------ Answer 04 ------------")
    print("\nAverage Price by Car Make:")
    print(make_price.round(2))

# --------------------------------------------------------------------------|
    year_power = horsepower_by_year(data)

    print("\n\n------------ Answer 05 ------------")
    print("\nAverage Horsepower by Year:")
    print(year_power)

# --------------------------------------------------------------------------|
    print("\n\n------------ Answer 06 ------------")
    price_horsepower_plot(data)

# --------------------------------------------------------------------------|
    print("\n\n------------ Answer 07 ------------")
    mph_histogram(data)

# --------------------------------------------------------------------------|
    costly_cars = expensive_cars(data)

    print("\n\n------------ Answer 08 ------------")
    print("\nCars above $500,000:")
    print(costly_cars)

# --------------------------------------------------------------------------|

    export_data(data)
    print("\n\n------------ Answer 09 ------------")
    print("Cleaned dataset saved successfully.\n")