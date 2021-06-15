a = int(input())
b = int(input())
n1 = int(input())
n2 = int(input())

min_1 = (n1 - 1) * a + n1
min_2 = (n2 - 1) * b + n2

max_1 = min_1 + 2 * a
max_2 = min_2 + 2 * b

if min_2 > max_1 or min_1 > max_2:
    print(-1)
else:
    print(max(min_1, min_2), min(max_1, max_2))

