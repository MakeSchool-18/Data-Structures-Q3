#!python

from queue import Queue
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = Queue()
        assert q.peek() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Queue(['A', 'B', 'C'])
        assert q.peek() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = Queue()
        assert q.length() == 0
        q.enqueue('A')
        assert q.length() == 1
        q.enqueue('B')
        assert q.length() == 2
        q.dequeue()
        assert q.length() == 1
        q.dequeue()
        assert q.length() == 0

    def test_peek(self):
        q = Queue()
        assert q.peek() is None
        q.enqueue('A')
        assert q.peek() == 'A'
        q.enqueue('B')
        assert q.peek() == 'A'
        q.dequeue()
        assert q.peek() == 'B'
        q.dequeue()
        assert q.peek() is None

    def test_enqueue(self):
        q = Queue()
        q.enqueue('A')
        assert q.peek() == 'A'
        assert q.length() == 1
        q.enqueue('B')
        assert q.peek() == 'A'
        assert q.length() == 2
        q.enqueue('C')
        assert q.peek() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_dequeue(self):
        q = Queue(['A', 'B', 'C'])
        assert q.dequeue() == 'A'
        assert q.length() == 2
        assert q.dequeue() == 'B'
        assert q.length() == 1
        assert q.dequeue() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()


if __name__ == '__main__':
    unittest.main()
