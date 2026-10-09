def trap_water(arr):

    left = 0
    right = len(arr) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        # Here I am checking the smaller side
        if arr[left] <= arr[right]:

            if arr[left] >= left_max:
                # Update the maximum height from left
                left_max = arr[left]

            else:
                # Water trapped at this position
                water += left_max - arr[left]

            left += 1

        else:
            if arr[right] >= right_max:
                # Update the maximum height from right
                right_max = arr[right]

            else:
                # Water trapped at this position
                water += right_max - arr[right]

            right -= 1

    return water


# Default input
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0]

# User input
# arr = list(map(int, input("Enter heights : ").split()))

result = trap_water(arr)
print("\nTotal water trapped is :", result,"\n")