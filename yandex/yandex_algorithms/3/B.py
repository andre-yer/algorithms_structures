def main():
    numbers_1 = set(map(int, input().split()))
    numbers_2 = set(map(int, input().split()))
    print(*sorted(numbers_1 & numbers_2))


if __name__ == '__main__':
    main()
