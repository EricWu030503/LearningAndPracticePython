# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    """
    Detects whether a cycle exists in a linked list using fast and slow pointers.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        bool: True if a cycle exists, False otherwise.
    """
    slow = head  # moves 1 step at a time
    fast = head  # moves 2 steps at a time

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # cycle detected

    return False  # no cycle
