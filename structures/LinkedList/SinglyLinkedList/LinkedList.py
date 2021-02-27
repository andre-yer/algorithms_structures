class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None
        self.tail = None
        # self.counter = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        if index >= self.size or index < 0:
            return -1
        else:
            for _ in range(index):
                curr = curr.next
            return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        list_node = ListNode(val)
        if not self.head:
            self.head = list_node
        else:
            curr = self.head
            self.head = list_node
            self.head.next = curr
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(self.size - 1):
                curr = curr.next
            curr.next = ListNode(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, 
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            pass
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            list_node = ListNode(val)
            list_node.next = curr.next
            curr.next = list_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            pass
        elif index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1


def main():
    pass



if __name__ == '__main__':
    main()
