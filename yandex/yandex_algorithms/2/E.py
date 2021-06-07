def id_max_val(dists, n):
    max_value = 0
    id_max = -1
    for i in range(n-1, -1, -1):
        if dists[i] >= max_value:
            max_value = dists[i]
            id_max = i
    return max_value, id_max

def place(dists, n):
    max_value, id_max = id_max_val(dists, n)
    vasya_dist = 0
    for i in range(1, n-1):
        if dists[i] % 10 == 5 and i > id_max and dists[i] > dists[i+1]:
            if vasya_dist < dists[i]:
                vasya_dist = dists[i]
    if not vasya_dist:
        return 0
    else:
        return len([item for item in dists if vasya_dist < item]) + 1

n = int(input())
dists = list(map(int, input().split()))
print(place(dists, n))