#!python

class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # TODO: initialize instance variables
        pass
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # TODO: check if empty
        pass

    def length(self):
        """Return the number of items in this queue"""
        # TODO: count number of items
        pass

    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        # TODO: return next item, if any
        pass

    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        # TODO: enqueue given item
        pass

    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        # TODO: dequeue next item, if any
        pass
