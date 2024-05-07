#Define the class named node *representing single node
class Node:
    # method for the Node class. Node will have two attributes: data and next.
    def __init__(self, data):
        #initialize the data attributes of the node with the given data
        self.data = data
        #Initialize the next attribute of the node as None, 
        #indicating that it initially does not point to any other nodeas its empty.
        self.next = None



