class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear = -1
        self.maxsize = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.maxsize
            self.queue[self.rear] = value
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxsize
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxsize


myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # return True
print(myCircularQueue.enQueue(2))  # return True
print(myCircularQueue.enQueue(3))  # return True
print(myCircularQueue.enQueue(4))  # return False
print(myCircularQueue.Rear())      # return 3
print(myCircularQueue.isFull())    # return True
print(myCircularQueue.deQueue())   # return True
print(myCircularQueue.enQueue(4))  # return True
print(myCircularQueue.Rear())      # return 4
