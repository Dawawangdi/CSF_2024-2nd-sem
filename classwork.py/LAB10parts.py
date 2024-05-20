
###Reversed Linked List :

class Solution:
    def reverseList(self, head):
        prev, curr = None, head  # Initializing pointers: prev points to None initially, curr points to the head
        
        while curr:  # Loop until curr is None, which means we've reached the end of the list
            next_node = curr.next  # Store the next node temporarily since we're about to change curr.next
            curr.next = prev  # Reverse the link: point the current node's next pointer to the previous node
            prev, curr = curr, next_node  # Move pointers forward: prev now points to the current node, curr moves to the next node
        
        return prev  # Return the new head of the reversed list


### Merge Two Sorted Lists:

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Initialize a dummy node as the head of the merged list.
        dummy = ListNode(-1)
        # Pointer 'current' to build the merged list.
        current = dummy
        
        # Merge lists until either list1 or list2 becomes empty.
        while list1 and list2:
            # Compare the values of current nodes in list1 and list2.
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move 'current' pointer to the next node.
            current = current.next
        
        # Attach remaining nodes of list1 or list2 to the merged list.
        current.next = list1 if list1 else list2
        
        # Return the head of the merged list.
        return dummy.next


###Remove Nth Node From End of List :
class Solution:
    def removeNthFromEnd(self, head, n):
        # Initialize a dummy node to simplify edge cases.
        dummy = ListNode(0, head)
        
        # Initialize two pointers: slow and fast.
        slow = fast = dummy
        
        # Move the 'fast' pointer n steps ahead.
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers until 'fast' reaches the last node.
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the Nth node from the end.
        slow.next = slow.next.next
        
        # Return the head of the modified list.
        return dummy.next
