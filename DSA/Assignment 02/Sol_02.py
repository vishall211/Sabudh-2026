class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_middle(head):
    # If the list has 0 or 1 node
    if head is None or head.next is None:
        return None

    slow = head
    fast = head

    # Find the node before the middle
    while fast and fast.next:
        fast = fast.next.next

        if fast and fast.next:
            slow = slow.next

    # Delete the middle node
    slow.next = slow.next.next

    return head


# Take input
values = list(map(int, input("\nEnter elements : ").split()))

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

# Delete middle
head = delete_middle(head)

# Print the result
print("Updated Elements : ")
current = head
while current:
    print(current.data, end=" ")
    current = current.next
print("\n")