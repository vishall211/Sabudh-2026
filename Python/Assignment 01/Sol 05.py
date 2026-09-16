# Write a program to calculate the sum of series up to n term.
# For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. This series is formed by appending the digit 2 in each term.

n = int(input("\nEnter n : "))

term = 0
total = 0
count = 0

while count < n :
    term = term * 10 + 2
    total = total + term
    count = count + 1
print("Sum of series upto n i.e",n," : ",total,"\n")