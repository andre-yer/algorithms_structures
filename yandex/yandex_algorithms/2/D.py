def smaller_neighbors(numbers):
    answer = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i + 1] and numbers[i] > numbers[i - 1]:
            answer += 1
    return answer


def main():
    numbers = list(map(int, input().split()))
    print(smaller_neighbors(numbers))


if __name__ == '__main__':
    main()
