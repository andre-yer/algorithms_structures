class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        if index >= self.size or index < 0:
            return -1
        else:
            for _ in range(index):
                curr = curr.next
            return curr.val

    def addAtHead(self, val: int) -> None:
        list_node = ListNode(val)
        if not self.head:
            self.head = list_node
        else:
            curr = self.head
            self.head = list_node
            self.head.next = curr
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(self.size - 1):
                curr = curr.next
            curr.next = ListNode(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
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

    def create_from_list(self, nodes: list) -> None:
        for item in nodes[::-1]:
            self.addAtHead(item)


def main():
    pass


if __name__ == '__main__':
    main()
