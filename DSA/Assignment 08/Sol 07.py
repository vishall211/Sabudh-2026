class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head

        # Find the length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Remove unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Connect the last node to the head
        tail.next = head

        # Find the new last node
        steps = length - k
        new_tail = tail

        while steps > 0:
            new_tail = new_tail.next
            steps -= 1

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head


def createList(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("NULL")


values = [10, 20, 30, 40, 50, 60]
k = 4

head = createList(values)

solution = Solution()
result = solution.rotateRight(head, k)

print("\nInput:", values, "k =", k)
print("Output:", end=" ")
printList(result)
print()
