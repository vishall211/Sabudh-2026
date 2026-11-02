# Question: Find two numbers that appear only once while all other numbers appear twice.

# Taking input
nums = list(map(int, input("\nEnter array elements: ").split()))
xor = 0

# Find XOR of all numbers
for x in nums:
    xor ^= x

# Get the rightmost set bit
bit = xor & -xor

num1 = 0
num2 = 0

# Separate numbers into two groups
for x in nums:
    if x & bit:
        num1 ^= x
    else:
        num2 ^= x

print("\nTwo unique numbers : ", num1, num2, "\n")