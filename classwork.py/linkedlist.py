##Python Code for Singly Linked List:

# Defineing a class named Node representing a single node in a singly linked list.
class Node:
    # Constructor to initialize a node with data and a pointer to the next node.
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

# Defineing a class named SinglyLinkedList representing a singly linked list.
class SinglyLinkedList:
    # Constructor to initialize the linked list with a head node.
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Method to append a new node with the given data to the end of the linked list.
    def append(self, data):
        # Create a new node with the given data.
        new_node = Node(data)
        
        # Check if the linked list is empty.
        if not self.head:
            self.head = new_node  # Set the new node as the head if the list is empty
            return
        
        # Traversing the linked list to find the last node.
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        # Set the next pointer of the last node to the new node.
        last_node.next = new_node

    # Method to display the elements of the linked list.
    def display(self):
        current = self.head  # Start from the head of the linked list
        while current:
            print(current.data, end=" -> ")  # Print the data of the current node
            current = current.next  # Move to the next node
        print("None")  # Print "None" to signify the end of the linked list

# Example usage:
# Create an instance of the SinglyLinkedList class.
sll = SinglyLinkedList()

# Append some elements to the linked list.
sll.append(1)
sll.append(2)
sll.append(3)

# Display the elements of the linked list.
sll.display()

