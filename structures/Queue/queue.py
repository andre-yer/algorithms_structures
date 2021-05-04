from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return -1

    def is_empty(self):
        return len(self.queue) == 0


def main():
    queue = Queue()
    queue.enqueue(2)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())


if __name__ == '__main__':
    main()
