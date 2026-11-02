# Question: Calculate the dot product of two sparse vectors efficiently.

class SparseVector:
    def __init__(self, nums):
        self.values = {}

        # Store only non-zero values with their indexes
        for i in range(len(nums)):
            if nums[i] != 0:
                self.values[i] = nums[i]

    def dotProduct(self, vec):
        total = 0

        # Multiply values having the same index
        for i in self.values:
            if i in vec.values:
                total += self.values[i] * vec.values[i]
        return total

# Taking input
nums1 = list(map(int, input("\nEnter first vector elements : ").split()))
nums2 = list(map(int, input("Enter second vector elements : ").split()))

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)

print("\nDot product : ", v1.dotProduct(v2))
print("\n")