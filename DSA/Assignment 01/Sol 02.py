def max_product_triplet(arr):

    # First i am sorting the array
    arr.sort()
    n = len(arr)

    # Product of last three numbers
    product1 = arr[n - 1] * arr[n - 2] * arr[n - 3]

    # Product of first two negative numbers and the last largest number
    product2 = arr[0] * arr[1] * arr[n - 1]

    # Here I am checking which product is greater
    if product1 > product2:
        return arr[n - 3], arr[n - 2], arr[n - 1]
    else:
        return arr[0], arr[1], arr[n - 1]


# Default input
arr = [-4, 1, -8, 9, 6]

# User input
# arr = list(map(int, input("Enter array elements : ").split()))

result = max_product_triplet(arr)
print("\nTriplet with maximum product is :", result,"\n")