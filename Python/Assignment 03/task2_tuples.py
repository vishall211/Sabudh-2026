# ---------------------------------------------------------------------------
# Part A: Tuple Creation and Access
# ---------------------------------------------------------------------------

# Q1. Create a tuple with different data types
def create_mixed_tuple():
    my_tuple = (10, 5.5, "Python", True)
    return my_tuple


# Q2. Create a tuple with five numbers and print one element
def get_tuple_element():
    numbers = (10, 20, 30, 40, 50)
    return numbers[2]   # Here i'll ge the value present at index 2


# Q3. Get the 4th element from the end
def get_fourth_from_end(my_tuple):
    if len(my_tuple) < 4:
        return "Tuple has fewer than 4 elements"
    return my_tuple[-4]     # Here i have used negative indexing to fetch the value from the end.




# ---------------------------------------------------------------------------
# Part B: Tuple Modification
# ---------------------------------------------------------------------------

# Q4. Add an item to a tuple
def add_item_to_tuple(my_tuple, item):
    my_list = list(my_tuple) # Here i am converting tuple to list
    my_list.append(item)     # Adding new item in a list

    new_tuple = tuple(my_list)  # Here i am converting list back to tuple
    return new_tuple




# ---------------------------------------------------------------------------
# Part C: Tuple Conversion
# ---------------------------------------------------------------------------

# Q5. Convert a tuple into a dictionary
def tuple_to_dictionary(my_tuple):
    # Create dictionary using index as key
    result = {}

    for i in range(len(my_tuple)):
        result[i] = my_tuple[i]
    return result




# ---------------------------------------------------------------------------
# Part D: Tuple Transformation in a List
# ---------------------------------------------------------------------------

# Q6. Replace the last element of each tuple with 100
def replace_last_element(tuple_list):
    result = []

    for my_tuple in tuple_list:
        new_tuple = my_tuple[:-1] + (100,)
        result.append(new_tuple)
    return result



if __name__ == "__main__":
# -----------------------------------------------------------------------------------|
    print("----- Part A : Tuple Creation and Access -----")

    # Ans 01
    print("Ans 01. Mixed tuple : ", create_mixed_tuple())

    # Ans 02
    print("Ans 02. Selected element : ", get_tuple_element())

    # Ans 03
    my_tuple = tuple(input("Enter tuple values separated by space : ").split())

    print("Ans 03. 4th element from the end : ", get_fourth_from_end(my_tuple))
    print("\n----- Part B : Tuple Modification -----")

    # Ans 04
    item = input("Enter an item to add : ")
    print("Ans 04. New tuple : ", add_item_to_tuple(my_tuple, item))

    print("\n----- Part C : Tuple Conversion -----")

    # Ans 05
    print("Q5. Dictionary : ", tuple_to_dictionary(my_tuple))
    print("\n----- Part D : Tuple Transformation -----")

    # Ans 06
    tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    print("Ans 06. Updated tuples : ", replace_last_element(tuple_list))