class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_one(head):
    # Reverse the list first
    head = reverse_list(head)

    current = head
    carry = 1

    # Add 1 from the last digit
    while current and carry:
        total = current.data + carry

        current.data = total % 10
        carry = total // 10

        if carry:
            if current.next is None:
                current.next = Node(0)

            current = current.next

    # Reverse again to get the original order
    return reverse_list(head)

def reverse_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

# Take input
values = list(map(int, input("Enter digits : ").split()))

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

# Add 1
head = add_one(head)

# Print the result
current = head

while current:
    print(current.data, end="")
    current = current.next