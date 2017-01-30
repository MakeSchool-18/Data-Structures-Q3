#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    def is_empty(self):
        """Return True if this linked list is empty, or False otherwise"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        node_count = 0
        current = self.head  # Start at the head node
        while current is not None:
            node_count += 1  # Count this node
            current = current.next  # Skip to the next node
        return node_count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)
        # Check if list is empty
        if self.head is None:
            self.head = new_node
        # Otherwise insert after tail node
        else:
            self.tail.next = new_node
        # Update tail node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)
        # Insert before head node
        new_node.next = self.head
        # Update head node
        self.head = new_node
        # Check if list was empty
        if self.tail is None:
            self.tail = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        current = self.head
        previous = None
        found = False
        # Find the given item
        while not found and current is not None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        # Delete if found
        if found:
            if current is not self.head and current is not self.tail:
                previous.next = current.next
                current.next = None
            if current is self.head:
                self.head = current.next
            if current is self.tail:
                if previous is not None:
                    previous.next = None
                self.tail = previous
        else:
            raise ValueError('Item not found: {}'.format(item))

    def find(self, condition):
        """Return an item in this linked list satisfying the given condition"""
        current = self.head  # Start at the head node
        while current is not None:
            if condition(current.data):
                return current.data
            current = current.next  # Skip to the next node
        return None


if __name__ == '__main__':
    test_linked_list()
