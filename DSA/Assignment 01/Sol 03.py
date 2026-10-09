def three_sum(nums):

    # Firstly i am sorting the array
    nums.sort()
    ans = []
    n = len(nums)

    for i in range(n - 2):

        # Skip duplicate numbers
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:

                # We found a valid triplet
                ans.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicates from left side
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicates from right side
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                # We need a bigger sum
                left += 1

            else:
                # We need a smaller sum
                right -= 1

    return ans


# Default input
nums = [-1, 0, 1, 2, -1, -4]

# User input
# nums = list(map(int, input("Enter numbers : ").split()))

result = three_sum(nums)
print("\nTriplets are :", result,"\n")