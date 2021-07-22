def symmetric_elem(numbers, n):
    answer = -1
    for i in range(n - 1):
        if numbers[i] != numbers[n - 1]:
            answer = i
        else:
            if is_symmetric(numbers[i:n]):
                return answer
            else:
                continue
    return answer


def is_symmetric(numbers):
    for i in range(len(numbers)):
        if numbers[i] != numbers[len(numbers) - 1 - i]:
            return False
    return True


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    elem = symmetric_elem(numbers, n)
    if elem == -1:
        print(0)
    else:
        print(elem + 1)
        print(*numbers[0:elem + 1][::-1])


if __name__ == '__main__':
    main()
