def arrangeNumbers(nums):

    # Check each number
    for i in range(len(nums)):

        # If the number is negative
        if nums[i] < 0:
            negative = nums[i]
            j = i

            # Move positive numbers one position right
            while j > 0 and nums[j - 1] >= 0:
                nums[j] = nums[j - 1]
                j -= 1

            # Put the negative number in the correct position
            nums[j] = negative
    return nums

# Checking function
nums1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(arrangeNumbers(nums1))
