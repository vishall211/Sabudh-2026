def productExceptSelf(nums):
    result = [1] * len(nums)

    # Calculate left-side products
    left = 1
    for i in range(len(nums)):
        result[i] = left
        left *= nums[i]

    # Calculate right-side products
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result


nums = list(map(int, input("\nEnter array elements: ").split()))

print("\nOutput :", productExceptSelf(nums), "\n")