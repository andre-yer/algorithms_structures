t_room, t_cond = map(int, input().split())
mode = input()
if (mode == 'heat' and t_room <= t_cond) or (mode == 'freeze' and t_room >= t_cond) or mode == 'auto':
    print(t_cond)
elif (mode == 'heat' and t_room > t_cond) or (mode == 'freeze' and t_room < t_cond) or mode == 'fan':
    print(t_room)

