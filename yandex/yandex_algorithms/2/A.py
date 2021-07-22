def is_growth(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True


def main():
    numbers = list(map(int, input().split()))
    if is_growth(numbers):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
