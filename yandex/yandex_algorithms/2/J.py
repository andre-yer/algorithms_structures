n = int(input())
prev = float(input())
min_v = 30.0 
max_v = 4000.0

for i in range(1, n):
    cur, s = input().split()
    cur = float(cur)
    if cur == prev:
        continue
    mid = (prev + cur)/2
    if cur > prev and s == 'closer' or cur < prev and s == 'further':
        min_v = max(min_v, mid)
    else:
        max_v = min(max_v, mid)
    prev = cur

print(min_v, max_v)