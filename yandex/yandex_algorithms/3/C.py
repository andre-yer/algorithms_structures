def cube_solution(anya_cubes, borya_cubes):
    return list(map(sorted, [anya_cubes & borya_cubes, anya_cubes - borya_cubes, borya_cubes - anya_cubes]))

n, m = map(int, input().split())
anya_cubes = set()
borya_cubes = set()
for i in range(n):
    anya_cubes.add(int(input()))
for i in range(m):
    borya_cubes.add(int(input()))
cubes_list = cube_solution(anya_cubes, borya_cubes)
for i in range(3):
    print(len(cubes_list[i]))
    print(*cubes_list[i])