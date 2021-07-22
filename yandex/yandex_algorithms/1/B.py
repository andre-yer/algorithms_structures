def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if (a + b > c) and (b + c > a) and (a + c > b):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
