# Problem 7: Count Consistent Strings

def countConsistentStrings(allowed, words):

    count = 0
    for word in words:

        # Check whether all characters are allowed
        if all(char in allowed for char in word):
            count += 1
    return count


allowed = input("Enter allowed characters: ")
words = input("Enter words separated by space: ").split()

print("\nOutput :", countConsistentStrings(allowed, words))