import unittest
from LinkedList import ListNode, MyLinkedList


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.result = []
        self.obj = MyLinkedList()

    def test_get_empty_list(self):
        self.result.append(self.obj.get(0))
        self.assertEqual(self.result, [-1, ])

    def test_add_head(self):
        self.obj.addAtHead(5)
        self.result.append(self.obj.get(0))
        self.obj.addAtHead(10)
        for i in range(2):
            self.result.append(self.obj.get(i))
        self.assertEqual(self.result, [5, 10, 5, ])

    def test_add_tail(self):
        self.obj.addAtTail(5)
        self.result.append(self.obj.get(0))
        self.obj.addAtHead(10)
        self.obj.addAtTail(15)
        for i in range(3):
            self.result.append(self.obj.get(i))
        self.assertEqual(self.result, [5, 10, 5, 15, ])

    def test_add_index(self):
        self.obj.addAtIndex(0, 5)
        self.result.append(self.obj.get(0))
        self.obj.addAtIndex(0, 10)
        for i in range(2):
            self.result.append(self.obj.get(i))
        self.obj.addAtIndex(1, 15)
        for i in range(3):
            self.result.append(self.obj.get(i))
        self.obj.addAtIndex(3, 20)
        for i in range(4):
            self.result.append(self.obj.get(i))
        self.assertEqual(self.result, [5, 10, 5, 10, 15, 5, 10, 15, 5, 20])

    def test_delete(self):
        for i in range(4):
            self.obj.addAtHead(i)
        self.obj.deleteAtIndex(0)
        for i in range(3):
            self.result.append(self.obj.get(i))
        self.obj.deleteAtIndex(1)
        for i in range(2):
            self.result.append(self.obj.get(i))
        self.assertEqual(self.result, [2, 1, 0, 2, 0])


if __name__ == '__main__':
    unittest.main()
