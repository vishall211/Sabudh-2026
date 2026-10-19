# Problem 8: Remove All Adjacent Duplicates in String

def removeDuplicates(s):

    stack = []
    for char in s:

        # Remove the character if it matches the top
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


s = input("\nEnter a string : ")
print("\nOutput :", removeDuplicates(s))