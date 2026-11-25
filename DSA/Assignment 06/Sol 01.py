
# Create a node for the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head):
        # Reverse the linked list
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev

        # Remove nodes smaller than the maximum value
        max_value = head.val
        curr = head

        while curr.next:
            if curr.next.val < max_value:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_value = curr.val

        # Reverse the list again
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


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
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


# Input data
values = [5, 2, 13, 3, 8]

# Run the solution
head = createList(values)

solution = Solution()
result = solution.removeNodes(head)

print("\nInput :", values)
print("Output :", end=" ")
printList(result)
print("\n")
