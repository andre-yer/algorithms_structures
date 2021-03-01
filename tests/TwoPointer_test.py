import unittest
from modules.LinkedList import ListNode, SinglyLinkedList
from structures.LinkedList.TwoPointerTechnique.TwoPointer import TwoPointer


class TwoPointerTest(unittest.TestCase):
    def setUp(self):
        self.obj = SinglyLinkedList()
        self.obj.create_from_list([0, 1, 2, 3, 4])

    def test_has_cycle_false(self):
        self.assertFalse(TwoPointer().hasCycle(self.obj.head))

    def test_has_cycle_true(self):
        self.obj.head.next.next.next = self.obj.head
        self.assertTrue(TwoPointer().hasCycle(self.obj.head))

    


if __name__ == '__main__':
    unittest.main()