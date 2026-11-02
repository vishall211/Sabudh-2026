# Question: Find the maximum sum of two equidistant nodes in a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def maximum_twin_sum(head):
    values = []

    # Store linked list values in a list
    while head:
        values.append(head.data)
        head = head.next

    max_sum = values[0] + values[-1]
    n = len(values)

    # Add elements from opposite ends
    for i in range(n // 2):
        total = values[i] + values[n - 1 - i]
        max_sum = max(max_sum, total)

    return max_sum

# Taking input
values = list(map(int, input("\nEnter even number of linked list elements : ").split()))

head = Node(values[0])
temp = head

# Creating the linked list
for x in values[1:]:
    temp.next = Node(x)
    temp = temp.next

print("\nMaximum twin sum:", maximum_twin_sum(head))
print("\n")