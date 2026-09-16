# Write a program to reverse given numbers without slicing. Input will be a positive integer.

number = int(input("\nEnter a positive integer : "))
print("\nOriginal Number : ",number)
reversed_no = 0

while number > 0:
    digit = number % 10
    reversed_no = reversed_no * 10 + digit
    number = number // 10
print("Reversed Number : ",reversed_no, "\n")