class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    # Move slow one step and fast two steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data


# Take input from the user
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

# Find and print the middle element
print("Middle element : ", find_middle(head))