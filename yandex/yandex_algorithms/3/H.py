def fallen_birds(birds):
    return len(set([item[0] for item in birds]))


def main():
    n = int(input())
    birds = [tuple(map(int, input().split())) for _ in range(n)]
    print(fallen_birds(birds))


if __name__ == '__main__':
    main()
