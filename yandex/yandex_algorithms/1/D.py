def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b == c == 0 or (a == 0 and b == c * c):
        print('MANY SOLUTIONS')
    elif c < 0 or (a == 0 and b != c * c):
        print('NO SOLUTION')
    elif (c * c - b) % a != 0:
        print('NO SOLUTION')
    else:
        print(int((c * c - b) / a))


if __name__ == '__main__':
    main()
