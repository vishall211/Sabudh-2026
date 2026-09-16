def chocolateDistribution(arr, m):
    arr.sort()      # Sort the packets

    # Store the minimum difference
    minimumDifference = float("inf")

    # Check each group of m packets
    for i in range(len(arr) - m + 1):
        difference = arr[i + m - 1] - arr[i]

        # Update minimum difference
        if difference < minimumDifference:
            minimumDifference = difference

    return minimumDifference

# Checking function
arr1 = [7, 3, 2, 4, 9, 12, 56]
print("Minimum Difference is", chocolateDistribution(arr1, 3))
