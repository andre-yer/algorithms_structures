def turtles_truth(n, turtles_say):
    been = set()
    answer = 0

    for say in turtles_say:
        non_neg = say[0] >= 0 and say[1] >= 0
        equal_n = say[0] + say[1] == n - 1
        if non_neg and equal_n and say not in been:
            answer += 1
            been.add(say)

    return answer


n = int(input())
turtles_say = [tuple(map(int, input().split())) for _ in range(n)]
print(turtles_truth(n, turtles_say))
