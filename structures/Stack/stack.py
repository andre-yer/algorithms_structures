class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value: int):
        self.stack.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1

    def isEmpty(self):
        return self.stack == []


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    main()
