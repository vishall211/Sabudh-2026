def countPairs(arr, k):
    count = 0       # Store the number of pairs

    # Check all possible pairs
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            # Check if the sum is equal to k
            if arr[i] + arr[j] == k:
                count += 1

    return count

# Checking function
arr1 = [1, 5, 7, -1]
print(countPairs(arr1, 6))
