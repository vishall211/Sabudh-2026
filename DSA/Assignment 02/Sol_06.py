class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_numbers(list1, list2):
    # Convert both linked lists into numbers
    num1 = 0
    num2 = 0

    current = list1

    while current:
        num1 = num1 * 10 + current.data
        current = current.next

    current = list2

    while current:
        num2 = num2 * 10 + current.data
        current = current.next

    total = num1 + num2

    # Convert the answer back into a linked list
    digits = list(map(int, str(total)))

    head = None
    tail = None

    for digit in digits:
        new_node = Node(digit)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


# Take input for first number
values1 = list(map(int, input("Enter first number digits: ").split()))

# Take input for second number
values2 = list(map(int, input("Enter second number digits: ").split()))


# Create first linked list
head1 = None
tail1 = None

for value in values1:
    new_node = Node(value)

    if head1 is None:
        head1 = new_node
        tail1 = new_node
    else:
        tail1.next = new_node
        tail1 = new_node


# Create second linked list
head2 = None
tail2 = None

for value in values2:
    new_node = Node(value)

    if head2 is None:
        head2 = new_node
        tail2 = new_node
    else:
        tail2.next = new_node
        tail2 = new_node


# Add both numbers
result = add_numbers(head1, head2)

# Print the result
current = result

while current:
    print(current.data, end="")
    current = current.next