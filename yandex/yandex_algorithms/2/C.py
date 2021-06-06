def nearest(numbers, x):
    minimal = abs(numbers[0] - x)
    answer = numbers[0]
    for item in numbers:
        if abs(item - x) < minimal:
            minimal = abs(item - x)
            answer = item
    return answer

size = int(input())
numbers = list(map(int, input().split()))
x = int(input())
print(nearest(numbers, x))