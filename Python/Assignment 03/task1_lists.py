# ---------------------------------------------------------------------------
# Part A: Integer List Operations
# ---------------------------------------------------------------------------

# Q1. Multiply all items in the list
def multiply_items(nums):
    result = 1

    for num in nums:
        result = result * num
    return result


# Q2. Find the largest number
def find_largest(nums):
    return max(nums)


# Q3. Find the smallest number
def find_smallest(nums):
    return min(nums)


# Q4. Remove duplicate elements
def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)
    return result


# Q5. Check whether the list is empty
def check_empty(nums):
    return len(nums) == 0


# Q6. Find the largest odd number
def find_largest_odd(nums):
    odd_nums = []

    for num in nums:
        if num % 2 != 0:
            odd_nums.append(num)

    if len(odd_nums) == 0:
        return "No odd numbers found"
    return max(odd_nums)


# Q7. Remove elements at index 0, 4 and 5
def remove_indexes(nums):
    indexes = [0, 4, 5]
    result = []

    for i in range(len(nums)):
        if i not in indexes:
            result.append(nums[i])
    return result




# ---------------------------------------------------------------------------
# Part B: Tuple List Sorting
# ---------------------------------------------------------------------------

# Q8. Sort tuples by the last element
def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[-1])




# ---------------------------------------------------------------------------
# Part C: Word List Analysis
# ---------------------------------------------------------------------------

# Q9. Count lowercase letters in all words
def count_lowercase_letters(words):
    count = 0

    for word in words:
        for letter in word:
            if letter.islower():
                count = count + 1
    return count




# ---------------------------------------------------------------------------
# Part D: Consecutive Element Extraction
# ---------------------------------------------------------------------------

# Q10. Find elements appearing exactly k times consecutively
def find_consecutive_elements(nums, k):
    result = []
    i = 0

    while i < len(nums):
        count = 1

        while i + count < len(nums) and nums[i] == nums[i + count]:
            count = count + 1

        if count == k:
            result.append(nums[i])
        i = i + count

    return result



if __name__ == "__main__":
# -----------------------------------------------------------------------------------|
    print("\n----- Part A: Integer List Operations -----")

    # Takingg integer list from the user
    nums = list(map(int, input("Enter integers separated by space : ").split()))

    # Ans 01
    print("Ans 01. Product:", multiply_items(nums))     

    # Ans 02
    if len(nums) > 0:       
        print("Ans 02. Largest number : ", find_largest(nums))
    else:
        print("Ans 02. List is empty")

    # Ans 03
    if len(nums) > 0:
        print("Ans 03. Smallest number : ", find_smallest(nums))
    else:
        print("Ans 03. List is empty")

    # Ans 04
    print("Ans 04. Without duplicates : ", remove_duplicates(nums))

    # Ans 05
    print("Ans 05. Is list empty ?", check_empty(nums))

    # Ans 06
    print("Ans 06. Largest odd number : ", find_largest_odd(nums))

    # Ans 07
    print("Ans 07. After removing indexes 0, 4 and 5 : ", remove_indexes(nums))

# -----------------------------------------------------------------------------------|
    print("\n----- Part B: Tuple List Sorting -----")

    # Ans 08
    tuple_list = []
    n = int(input("Enter number of tuples : "))

    for i in range(n):
        values = tuple(map(int, input("Enter tuple values separated by space : ").split()))
        tuple_list.append(values)

    print("Ans 08. Sorted tuples : ", sort_tuples(tuple_list))

# -----------------------------------------------------------------------------------|
    print("\n----- Part C : Word List Analysis -----")

    # Ans 09
    words = input("Enter words separated by space : ").split()
    print("Ans 09. Total lowercase letters:", count_lowercase_letters(words))

# -----------------------------------------------------------------------------------|
    print("\n----- Part D: Consecutive Element Extraction -----")

    # Ans 10
    k = int(input("Enter k : "))
    print("Ans 10. Elements appearing exactly", k, "times consecutively : ", find_consecutive_elements(nums, k))