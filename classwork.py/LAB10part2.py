##Merge Two Sorted Lists:

class Solution:
    # Function to merge two sorted lists
    def mergeTwoLists(self, list1, list2):
        # Initialize a dummy node
        dummy = self.ListNode(-1)
        current = dummy
        
        # Merge lists while both have nodes
        while list1 and list2:
            # Select smaller value node
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move to next node
            
        # Append remaining nodes
        current.next = list1 or list2
        
        return dummy.next  # Return merged list head
