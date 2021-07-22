def main():
    buttons = set(map(int, input().split()))
    numbers = set(map(int, list(input())))
    print(len(numbers - buttons))


if __name__ == '__main__':
    main()
