class Solution:
    def lengthOfLIS(self, nums):
        result = []

        for num in nums:
            left = 0
            right = len(result)

            # Find the correct position for the number
            while left < right:
                mid = (left + right) // 2

                if result[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(result):
                result.append(num)
            else:
                result[left] = num

        return len(result)


nums = [10, 9, 2, 5, 3, 7, 101, 18]

solution = Solution()
result = solution.lengthOfLIS(nums)

print("\nInput:", nums)
print("Output:", result, "\n")
