class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    previous = None
    current = head

    # Reverse the links one by one
    while current:
        next_node = current.next
        current.next = previous

        previous = current
        current = next_node

    return previous

# Take input
values = list(map(int, input("Enter elements: ").split()))

# Create the linked list
head = None
tail = None

for value in values:
    new_node = Node(value)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

# Reverse the list
head = reverse_list(head)

# Print the reversed list
current = head

while current:
    print(current.data, end=" ")
    current = current.next
print("\n")