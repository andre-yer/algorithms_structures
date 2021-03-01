# import sys
# import os
# sys.path.append(os.path.abspath('../algorithms_structures'))
from modules.LinkedList import ListNode, SinglyLinkedList


class TwoPointer:
    def hasCycle(self, head: ListNode) -> bool:
        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False


def main():
    pass


if __name__ == '__main__':
    main()
