def n_unique_numbers(numbers):
    return len(set(numbers))

numbers = list(map(int, input().split()))
print(n_unique_numbers(numbers))