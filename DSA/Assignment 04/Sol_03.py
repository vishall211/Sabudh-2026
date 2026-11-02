# Question: Merge two sorted linked lists into one sorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(list1, list2):
    dummy = Node(0)
    temp = dummy

    # Compare both lists and connect the smaller node
    while list1 and list2:
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next

        temp = temp.next

    # Connect remaining nodes
    if list1:
        temp.next = list1
    else:
        temp.next = list2
    return dummy.next

def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Taking input
list1 = list(map(int, input("\nEnter first sorted linked list: ").split()))
list2 = list(map(int, input("Enter second sorted linked list: ").split()))

head1 = None
head2 = None

# Creating first linked list
temp = None
for x in list1:
    new_node = Node(x)

    if head1 is None:
        head1 = new_node
        temp = new_node
    else:
        temp.next = new_node
        temp = new_node

# Creating second linked list
temp = None
for x in list2:
    new_node = Node(x)

    if head2 is None:
        head2 = new_node
        temp = new_node
    else:
        temp.next = new_node
        temp = new_node

# Merge both lists
result = merge_lists(head1, head2)

print("\nMerged linked list")
print_list(result)
print("\n")