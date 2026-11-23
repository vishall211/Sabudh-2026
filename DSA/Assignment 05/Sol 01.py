# Create a node for the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move to the node before left
        for i in range(left - 1):
            prev = prev.next
        curr = prev.next

        # Reverse the required part
        for i in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next

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
left = 2
right = 4

# Run the solution
head = createList(values)

solution = Solution()
result = solution.reverseBetween(head, left, right)

print("\nInput:", values)
print("\nLeft:", left)
print("Right:", right)
print("\nOutput:", end=" ")
printList(result)
print("\n")