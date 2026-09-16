# Read an integer N. For all non-negative integers i < N, print i^2 as a list. 

user_input = int(input("\nEnter any integer : "))
result = []

i = 0;
while i < user_input:
    square = i * i;
    result.append(square)
    i = i + 1
print("Sqaure of integers from 0 to",user_input,"are : ",result,"\n")