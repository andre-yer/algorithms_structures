def smaller_neighboors(numbers):
    answer = 0
    for i in range(1, len(numbers)-1):
        if numbers[i] > numbers[i+1] and numbers[i] > numbers[i-1]:
            answer += 1
    return answer

numbers = list(map(int, input().split()))
print(smaller_neighboors(numbers))