# Write a program to display only those numbers from a list that satisfy the following conditions: 
# 1. The number must be divisible by 5
# 2. If the number is greater than 150, then skip it and move to the next number
# 3. If the number is greater than 500, then stop the loop

user_input = input("\nEnter numbers separated by commas : ")
numbers = user_input.split(",")
result = []

i = 0
while i < len(numbers):
    num = int(numbers[i].strip())

    if num > 500:
        break

    if num > 150:
        i = i + 1
        continue

    if num % 5 == 0:
        result.append(num)

    i = i + 1

print("The numbers are : ",result,"\n")