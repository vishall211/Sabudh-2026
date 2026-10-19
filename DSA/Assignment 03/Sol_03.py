# Problem 3: Add Two Numbers (Linked List)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:

        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0

        total = num1 + num2 + carry

        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


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


l1 = createList([2, 4, 3])
l2 = createList([5, 6, 4])

result = addTwoNumbers(l1, l2)

printList(result)