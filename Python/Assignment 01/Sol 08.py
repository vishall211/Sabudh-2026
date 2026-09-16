# Write a Python program to find the median of three values. Median means the middle value after sorting the three numbers.

a = int(input("\nInput 1st number : "))
b = int(input("Input 2nd number : "))
c = int(input("Input 3rd number : "))

if (a >= b and a <= c) or (a <= b and a >= c):
    median = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    median = b
else:
    median = c
print("\nMedian value is :",median,"\n")