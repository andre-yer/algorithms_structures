def simmetric_elem(numbers, n):
    answer = -1
    for i in range(n-1):
        if numbers[i] != numbers[n-1]:
            answer = i  
        else:
            if is_simmetric(numbers[i:n]):
                return answer
            else: 
                continue
    return answer

def is_simmetric(numbers):
    for i in range(len(numbers)):
        if numbers[i] != numbers[len(numbers)-1-i]:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))
elem = simmetric_elem(numbers, n)
if elem == -1:
    print(0)
else:
    print(elem+1)
    print(*numbers[0:elem+1][::-1])


