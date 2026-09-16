# Write a program to use a loop to display elements from a given list present at an odd index position. Odd index refers to index position (1, 3, 5, …), not odd numbers.

user_input = input("\nEnter numbers separated by commas : ")

numbers = user_input.split(",")
result = []

i = 0
while i < len(numbers):
    if i % 2 != 0:
        result.append(int(numbers[i].strip()))
    i = i + 1
print("Numbers are : ",result, "\n")