class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head

    # Check every node with the next node
    while current and current.next:

        if current.data == current.next.data:
            # Remove the duplicate node
            current.next = current.next.next
        else:
            current = current.next

    return head

# Take input
values = list(map(int, input("\nEnter sorted elements : ").split()))

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

# Remove duplicates
head = remove_duplicates(head)

# Print the result
current = head

while current:
    print(current.data, end=" ")
    current = current.next
print("\n")