class Node:
    """Represents the a single list node
    """

    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    """Singly Linked List class
    """

    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        """Adds a node to the head of the linked list

        Arguments:
            value {value} -- value to be inserted at the head of the list
        """
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        """Checks if a value is in the list

        Arguments:
            value {int} -- value to be checked for

        Returns:
            bool -- True if found and False otherwise
        """
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        """Reverses the linked list recursively
        """
        # if the list is empty return
        if self.head is None:
            return

        # write a recursive function that takes current node and previous
        def reverse_recursive(current_node, prev_node):
            # state a base case of if current.next is None set it as head
            # that is, if tail node
            if current_node.next_node is None:
                self.head = current_node
                # set the current.next to the previous
                current_node.next_node = prev_node
                # return
                return

            # otherwise
            # set the new_current to current.next
            new_current = current_node.next_node
            # set current.next to the prev
            current_node.next_node = prev_node
            # call the function recursively and pass new_current as current and current as previous
            reverse_recursive(new_current, current_node)

        # call the recursive function with head and none
        reverse_recursive(self.head, None)
