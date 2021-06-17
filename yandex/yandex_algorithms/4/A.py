def synonym(words, syn_dict):
    syn_dict[words[0]] = words[1]
    syn_dict[words[1]] = words[0]
    return syn_dict


n = int(input())
syn_dict = {}
for _ in range(n):
    syn_dict = synonym(input().split(), syn_dict)
print(syn_dict[input()])
