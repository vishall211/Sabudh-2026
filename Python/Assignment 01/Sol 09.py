# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    if n < 0:
        return "Opps!! It's a negative integer ) :"
    
    result = 1
    i = 1
    
    while i <= n:
        result = result * i
        i = i + 1
    
    return result

num = int(input("\nEnter a number : "))
print("Factorial of a number : ",factorial(num),"\n")