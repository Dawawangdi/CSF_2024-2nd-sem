###Reversed Linked List:

class Solution:
    # Function to reverse a linked list
    def reverseList(self, head):
        # Initialize pointers
        prev, curr = None, head
        
        # Traverse the list and reverse links
        while curr:
            next_node = curr.next  # Store next node
            curr.next = prev       # Reverse link
            prev, curr = curr, next_node  # Move pointers
            
        return prev  # Return new head

