from bisect import bisect_left
def successful_pairs(spells, potions, success):

    # Sort potions so we can use binary search
    potions.sort()

    ans = []
    n = len(potions)

    for spell in spells:
        # Find the minimum potion value needed
        needed = success / spell

        # Find the first potion greater than or equal to the required value
        index = bisect_left(potions, needed)

        # All potions after this index will work
        count = n - index

        ans.append(count)

    return ans


# Default input
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7

# User input
# spells = list(map(int, input("Enter spells : ").split()))
# potions = list(map(int, input("Enter potions : ").split()))
# success = int(input("Enter success value : "))

result = successful_pairs(spells, potions, success)
print("\nSuccessful pairs are : ", result,"\n")
print("\n")