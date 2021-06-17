def pyramid(blocks_list):
    blocks_dict = {}
    for w, h in blocks_list:
        if w not in blocks_dict:
            blocks_dict[w] = 0
        blocks_dict[w] = max(blocks_dict[w], h)
    return sum(blocks_dict.values())


n = int(input())
blocks_list = []
for _ in range(n):
    blocks_list.append(tuple(map(int, input().split())))
print(pyramid(blocks_list))
