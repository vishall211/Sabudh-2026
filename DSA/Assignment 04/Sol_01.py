# Question: Insert a new node at the beginning of a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, value):
    # Create a new node and connect it to the current head
    new_node = Node(value)
    new_node.next = head
    return new_node

def print_list(head):
    while head:
        print(head.data, end="")
        if head.next:
            print("->", end="")
        head = head.next
    print()

# Taking input
values = list(map(int, input("\nEnter linked list elements : ").split()))
value = int(input("\nEnter value to insert : "))

head = None
tail = None

# Creating the linked list
for x in values:
    new_node = Node(x)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

# Insert the new node
head = insert_at_beginning(head, value)

print("\nUpdated linked list : ")
print_list(head)
print("\n")