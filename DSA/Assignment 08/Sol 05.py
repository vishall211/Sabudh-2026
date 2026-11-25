class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def insertBeforeMiddle(self, head, value):
        if head is None:
            return ListNode(value)

        slow = head
        fast = head
        prev = None

        # Find the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Insert the new node before the middle
        new_node = ListNode(value)

        if prev is None:
            new_node.next = head
            return new_node

        prev.next = new_node
        new_node.next = slow

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

    print("->".join(result))


values = [1, 2, 3, 4, 5]
insert_value = 9

head = createList(values)

solution = Solution()
result = solution.insertBeforeMiddle(head, insert_value)

print("\nInput:", values)
print("Insert Value:", insert_value)
print("Output:", end=" ")
printList(result)
print()
