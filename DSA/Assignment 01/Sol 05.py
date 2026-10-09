def next_permutation(nums):
    n = len(nums)

    # Starting from right, here I am finding the first number smaller than the next number
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # If such a number is found
    if i >= 0:
        j = n - 1

        # Here I am finding the next greater number
        for j in range(n - 1, i, -1):
            if nums[j] > nums[i]:
                break

        # Swap both numbers
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the remaining part so ultimately it gives the next permutation
    left = i + 1
    right = n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]

        left += 1
        right -= 1

    return nums


# Default input
nums = [1, 2, 3]

# User input
# nums = list(map(int, input("Enter numbers : ").split()))

result = next_permutation(nums)
print("\nNext permutation is :", result,"\n")