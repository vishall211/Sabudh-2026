class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Start counting only from the beginning of a sequence
            if num - 1 not in num_set:
                count = 1
                current = num

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest


nums = [100, 4, 200, 1, 3, 2]

solution = Solution()
result = solution.longestConsecutive(nums)

print("\nInput:", nums)
print("Output:", result, "\n")
