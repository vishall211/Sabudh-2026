# Question: Find the maximum sum of a continuous subarray.

# Taking input
nums = list(map(int, input("\nEnter array elements : ").split()))

current_sum = nums[0]
max_sum = nums[0]

# Apply Kadane's Algorithm
for i in range(1, len(nums)):

    # Choose between starting new or continuing current subarray
    current_sum = max(nums[i], current_sum + nums[i])

    # Update maximum sum
    max_sum = max(max_sum, current_sum)

print("\nMaximum subarray sum :", max_sum, "\n")