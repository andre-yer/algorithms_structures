def table_size(a1, b1, a2, b2):
    square_dict = {}
    square_dict[(a1 + a2) * max(b1, b2)] = ((a1 + a2), max(b1, b2))
    square_dict[(a1 + b2) * max(b1, a2)] = ((a1 + b2), max(b1, a2))
    square_dict[(b1 + a2) * max(a1, b2)] = ((b1 + a2), max(a1, b2))
    square_dict[(b1 + b2) * max(a1, a2)] = ((b1 + b2), max(a1, a2))
    return square_dict[min(square_dict.keys())]


def main():
    a1, b1, a2, b2 = map(int, input().split())
    print(*table_size(a1, b1, a2, b2))


if __name__ == '__main__':
    main()
