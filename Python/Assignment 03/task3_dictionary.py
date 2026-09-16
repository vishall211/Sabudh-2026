# ---------------------------------------------------------------------------
# Part A: Sorting a Dictionary by Value
# ---------------------------------------------------------------------------

# Q1. Sort dictionary by value
def sort_by_value(data):
    ascending = dict(sorted(data.items(), key=lambda x: x[1]))
    descending = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

    return ascending, descending



# ---------------------------------------------------------------------------
# Part B: Iterating Through a Dictionary
# ---------------------------------------------------------------------------

# Q2. Iterate through dictionary
def iterate_dictionary(data):
    print("Keys:")

    for key in data:
        print(key)

    print("Values:")

    for value in data.values():
        print(value)

    print("Key-Value pairs:")

    for key, value in data.items():
        print(key, value)


# ---------------------------------------------------------------------------
# Part C: Merging Dictionaries
# ---------------------------------------------------------------------------

# Q3. Merge two dictionaries
def merge_dictionaries(data1, data2):
    result = data1.copy()
    result.update(data2)

    return result



# ---------------------------------------------------------------------------
# Part D: Aggregation Operations
# ---------------------------------------------------------------------------

# Q4. Find sum of all values
def find_sum(data):
    if len(data) == 0:
        return 0

    total = 0
    for value in data.values():
        total = total + value
    return total


# Q5. Find product of all values
def find_product(data):
    if len(data) == 0:
        return 0

    result = 1
    for value in data.values():
        result = result * value
    return result



# ---------------------------------------------------------------------------
# Part E: Sorting by Key
# ---------------------------------------------------------------------------

# Q6. Sort dictionary by key
def sort_by_key(data):
    return dict(sorted(data.items()))



# ---------------------------------------------------------------------------
# Part F: Removing Duplicates
# ---------------------------------------------------------------------------

# Q7. Remove duplicate values
def remove_duplicate_values(data):
    result = {}

    for key, value in data.items():
        if value not in result.values():
            result[key] = value

    return result


if __name__ == "__main__":
# -----------------------------------------------------------------------------------|
    data = {}
    n = int(input("Enter number of items : "))

    for i in range(n):
        key = input("Enter key : ")
        value = int(input("Enter numeric value : "))
        data[key] = value



    print("\n----- Part A : Sorting by Value -----")

    # Ans 01
    ascending, descending = sort_by_value(data)

    print("Ans 01. Ascending order :", ascending)
    print("Ans 02. Descending order :", descending)



    print("\n----- Part B : Iterating Through Dictionary -----")

    # Ans 02
    print("Ans 02.")
    iterate_dictionary(data)



    print("\n----- Part C: Merging Dictionaries -----")

    data2 = {} # Taking input from the user and this the second dictionary.
    n = int(input("Enter number of items for second dictionary : "))

    for i in range(n):
        key = input("Enter key : ")
        value = int(input("Enter numeric valuev : "))
        data2[key] = value


    # Ans 03
    print("Ans 03. Merged dictionary : ", merge_dictionaries(data, data2))



    print("\n----- Part D : Aggregation Operations -----")

    # Ans 04
    print("And 04. Sum of values : ", find_sum(data))

    # Ans 05
    print("Ans 05. Product of values : ", find_product(data))



    print("\n----- Part E : Sorting by Key -----")

    # Ans 06
    print("Ans 06. Sorted by key : ", sort_by_key(data))



    print("\n----- Part F : Removing Duplicate Values -----")

    # Ans 07
    print("Ans 07. Without duplicate values :", remove_duplicate_values(data))