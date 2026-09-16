#  You have been given a string. You need to remove all the duplicates from the string. The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can traverse the string only once.

user_input = input("\nEnter a string : ")
seen = set()
result = " "

i = 0
while i < len(user_input):
    char = user_input[i]

    if char not in seen :
        result = result + char
        seen.add(char)

    i = i + 1

print("Final String (without duplicate characters) : ",result,"\n")