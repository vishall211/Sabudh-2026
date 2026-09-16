def longest_subarray(arr, k):

    # Here I am storing sum and its first index
    seen = {0: -1}
    total = 0
    max_len = 0

    for i in range(len(arr)):

        # Adding the current number to total
        total += arr[i]

        # If total - k is already present, then we found a subarray with sum k
        if total - k in seen:
            length = i - seen[total - k]
            max_len = max(max_len, length)

        # Store only the first index of the sum
        if total not in seen:
            seen[total] = i

    return max_len


# Default input 
arr = [10, 5, 2, 7, 1, -10]
k = 15

# User input...pls dont use this..just for checking the program sabudh team.
# arr = list(map(int, input("Enter array elements : ").split()))
# k = int(input("Enter k : "))

result = longest_subarray(arr, k)
print("\nLongest subarray length is :", result,"\n")