def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    brick_list = sorted([a, b, c])
    a_min, b_min = brick_list[0], brick_list[1]
    if (a_min <= d and b_min <= e) or (a_min <= e and b_min <= d):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
