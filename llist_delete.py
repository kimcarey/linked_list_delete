'''
LUCID PROGRAMMING REVIEW: LINKED LIST
    - Builds on Insertion review and adds methods to delete nodes from linked list
'''

# Create class for node
class Node:
    # Create constructor and give it the argument of self and data
    # Data argument since we need to tell it what to pass into this node
    def __init__(self, data):
        self.data = data
        # Set self to None initially
        self.next = None


# Create class for linked list
class LinkedList:
    # Constructor
    def __init__(self):
        # Start of the list gets a head pointer
        self.head = None

    # function to print out the entries of a list
    # takes self as an argument because it's a Class function
    def print_list(self):
        current_node = self.head
        # While current_node is not NULL
        while current_node:
            print(current_node.data)
            # Move to next node in the list
            current_node = current_node.next

    # Function to append item to end of linked list
    def append(self, data):
        # First Case: If the linked list is empty and we need to append the first node
        # Create new node object and pass "data" as argument since the Node class takes an argument
        new_node = Node(data)

        # check if head of list is empty
        if self.head is None:
            self.head = new_node
            return

        # Next Case: If the linked list is not empty, we need to move the head pointer through each of the nodes
        # in the list to see where the end of the list is, so that we know where to input the new node
        # Define last_node and initially be equal to the head (b/c we're at the start of the list)
        last_node = self.head
        # While the next pointer of the node that we're currently on is not NULL, continue on the loop
        while last_node.next:
            # Move the head pointer to the right
            last_node = last_node.next
        # When loop has concluded last_node will point to the last node and now we can append node to end of list
        last_node.next = new_node


    # Function to prepend item to start of linked list
    def prepend(self, data):
        # Create new node object and pass "data" as argument since the Node class takes an argument
        new_node = Node(data)

        # We want the new node to point to the head (since we are prepending the new node to the start of the list)
        new_node.next = self.head
        # Set head to new node
        self.head = new_node


    # Function to insert item between two existing nodes in a linked list
    # Takes self since it's a Class function, previous node (so that we know what to insert after), and data
    def insert_after_node(self, prev_node, data):
        # If the prev_node (not we want to insert after) is not there; return
        if not prev_node:
            print('Previous node is not in the list')
            return

        # If prev_node is there, then create new node object
        new_node = Node(data)
        # Set new_node pointer to what prev_node is pointing to
        new_node.next = prev_node.next
        # Set prev_node pointer to new node
        prev_node.next = new_node



    # Function to delete node with a certain data field
    # Takes self as it is a Class function and key (data field for the node to be deleted)
    def delete_node(self, key):
        # CASE NO. 1: Node to be deleted is the head
        # Create current node and set to head of the list
        current_node = self.head

        # If current node is not empty and it's data field matches the key that we want to delete
        if current_node and current_node.data == key:
            # Set head to the next node is the list (the next node following original head)
            self.head = current_node.next
            # Remove current element from the list by setting it equal to None
            current_node = None
            return

        # CASE NO. 2: Node to be deleted is not the head
        # Find node in the list that consists of the key we're looking for
        # Need to keep track of the node preceding the node with the key we're looking for
        prev = None

        # Use loop to move head pointer along the list and keep track of both the current and previous nodes
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # Element is not present
        if current_node is None:
            return

        # If element is present
        # Moves previous node's pointer to what current node (one to be deleted) was pointing to
        prev.next = current_node.next
        # Remove element from the list
        current_node = None


    # Function to delete node with a certain position
    def delete_node_at_position(self, position):
        # CASE NO.1: Delete node with a 0 position
        current_node = self.head

        # If position to delete is the first position, set head to the following node
        if position == 0:
            self.head = current_node.next
            current_node = None
            return

        # CASE NO.2: Delete node with any other position
        # Go through the loop and check if the node in the position we want to delete
        # Need to keep track of previous node; initially set to None
        prev = None
        # Need to keep track of where the node is; set to 1 since we've accounted for a case with position 0
        count = 1

        while current_node and count != position:
            prev = current_node
            current_node = current_node.next
            count += 1

        # Do a check - If current node is None, then we know we've exceeded the position (situation where we have been
        # given a position that is higher than the number of elements in the list)
        if current_node is None:
            return

        # Moves previous node's pointer to what current node (one to be deleted) was pointing to
        prev.next = current_node.next
        # Remove element from the list
        current_node = None






# Define a linked list object
llist = LinkedList()

# Function calls to append
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')

# # Function call to prepend
# llist.prepend('E')

# # Function call to insert between nodes
# llist.insert_after_node(llist.head.next, 'E ')

# # Delete node (not head)
# llist.delete_node('B')

# Delete node with certain position
llist.delete_node_at_position(0)

llist.print_list()