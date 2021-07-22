def biggest_multiplication(numbers):
    if len(numbers) == 3:
        return sorted(numbers)
    else:
        max_1 = float('-inf')
        max_2 = None
        max_3 = None
        min_1 = float('+inf')
        min_2 = None
        for i in range(len(numbers)):
            if numbers[i] >= max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = numbers[i]
            elif numbers[i] >= max_2:
                max_3 = max_2
                max_2 = numbers[i]
            elif numbers[i] >= max_3:
                max_3 = numbers[i]
            if numbers[i] <= min_1:
                min_2 = min_1
                min_1 = numbers[i]
            elif numbers[i] <= min_2:
                min_2 = numbers[i]
        if max_1 * max_2 * max_3 > max_1 * min_1 * min_2:
            return max_1, max_2, max_3
        else:
            return min_1, min_2, max_1


def main():
    numbers = list(map(int, input().split()))
    print(*biggest_multiplication(numbers))


if __name__ == '__main__':
    main()
