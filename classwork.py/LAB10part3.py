##Remove Nth Node From End of List:

class Solution:
    # Function to remove Nth node from end of list
    def removeNthFromEnd(self, head, n):
        # Create a dummy node and set pointers
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast pointer to Nth node
        for _ in range(n):
            fast = fast.next

        # Move both pointers until end
        while fast.next:
            slow, fast = slow.next, fast.next

        # Remove Nth node
        slow.next = slow.next.next

        return dummy.next  # Return head of modified list

