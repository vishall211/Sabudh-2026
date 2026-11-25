class Solution:
    def findSmallestMissing(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left


nums = [0, 1, 2, 6, 9, 11, 15]

solution = Solution()
result = solution.findSmallestMissing(nums)

print("\nInput:", nums)
print("Output: The smallest missing element is", result, "\n")
