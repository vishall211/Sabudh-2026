# Problem 4: Merge K Sorted Lists

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    min_heap = []

    # Heree i am adding the first node of each list
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

    dummy = ListNode()
    current = dummy

    while min_heap:

        # Get the smallest node
        value, i, node = heapq.heappop(min_heap)

        current.next = node
        current = current.next

        # Add the next node from the same list
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next