def n_unique_numbers(numbers):
    return len(set(numbers))


def main():
    numbers = list(map(int, input().split()))
    print(n_unique_numbers(numbers))


if __name__ == '__main__':
    main()
