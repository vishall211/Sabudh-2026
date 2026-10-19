# Problem 6: Remove Duplicates from Sorted Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):

    current = head
    while current and current.next:

        # Skip the duplicate node
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


def createList(nums):
    dummy = ListNode()
    current = dummy

    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def printList(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next
    print(result)


head = createList([1, 1, 2, 3, 3])
result = deleteDuplicates(head)

printList(result)