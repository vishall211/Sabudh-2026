def threeSum(nums):
    result = []     # Store the triplets

    # Check all possible triplets
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):

                # Check if the sum is 0
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])

                    # Add only if it is not already present
                    if triplet not in result:
                        result.append(triplet)
    return result

# Checking function
print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))