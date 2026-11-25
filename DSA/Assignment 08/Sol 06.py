class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteLastOccurrence(self, head, key):
        curr = head
        last = None
        prev = None
        last_prev = None

        # Find the last occurrence
        while curr:
            if curr.val == key:
                last = curr
                last_prev = prev

            prev = curr
            curr = curr.next

        # If the value is not found
        if last is None:
            return head

        # Delete the last occurrence
        if last_prev is None:
            head = head.next
        else:
            last_prev.next = last.next

        return head


def createList(values):
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def printList(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print("->".join(result) + "->NULL")


values = [1, 2, 3, 4, 5, 4, 4]
key = 4

head = createList(values)

solution = Solution()
result = solution.deleteLastOccurrence(head, key)

print("\nInput:", values)
print("Delete Value:", key)
print("Output:", end=" ")
printList(result)
print()
