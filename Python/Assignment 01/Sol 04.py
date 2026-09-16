# Write a program to count the total number of digits in a number using a while loop.

number = int(input("\nEnter a number : "))
count = 0

if number == 0:
    count = 1
else:
    while number != 0:
        number = number // 10
        count = count + 1
print("Count of total no of digits : ",count, "\n")