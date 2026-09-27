class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_second_last(head):
    # We need at least two nodes
    if head is None or head.next is None:
        return None

    current = head

    # Stop at the second last node
    while current.next.next:
        current = current.next

    return current.data

# Take input
values = list(map(int, input("Enter elements : ").split()))

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

# Find second last element
answer = find_second_last(head)

print("Second last element:", answer)