
# Create a node for the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None:
            return head

        odd = head
        even = head.next
        even_head = even

        # Separate odd and even position nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # Connect odd and even lists
        odd.next = even_head
        return head

# Create linked list from input data
def createList(values):
    dummy = ListNode()
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next

# Print linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Input data
values = [1, 2, 3, 4, 5]

# Run the solution
head = createList(values)

solution = Solution()
result = solution.oddEvenList(head)

print("\nInput:", values)
print("\nOutput:", end=" ")
printList(result)
print("\n")
