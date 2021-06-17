def keyboard_usage(n, limits, order):
    keyboard_dict = {}
    for i in range(1, n + 1):
        keyboard_dict[i] = limits[i - 1]
    for item in order:
        keyboard_dict[item] -= 1
    for i in range(1, n + 1):
        if keyboard_dict[i] >= 0:
            print('NO')
        else:
            print('YES')


n = int(input())
limits = list(map(int, input().split()))
k = int(input())
order = list(map(int, input().split()))
keyboard_usage(n, limits, order)
