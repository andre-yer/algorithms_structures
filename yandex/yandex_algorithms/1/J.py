a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

main_det = a*d - b*c
det_x = e*d - b*f
det_y = a*f - c*e

if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
elif main_det == 0 and (det_x != 0 or det_y != 0):
    print(0)
elif a == 0 and c == 0 and det_x != 0:
    print(0)
elif b == 0 and d == 0 and det_y != 0:
    print(0)
elif a == 0 and b == 0 and e != 0:
    print(0)
elif c == 0 and d == 0 and f != 0:
    print(0)
elif main_det == 0 and (det_x == 0 or det_y == 0):
    if b == 0 and d == 0:
        if a != 0:
            print(3, e / a)
        elif c != 0:
            print(3, f / c)
    elif a == 0 and c == 0:
        if b != 0:
            print(4, e / b)
        elif d != 0:
            print(4, f / d)
    elif b != 0:
        print(1, -a / b, e / b)
    elif d != 0:
        print(1, -c / d, f / d)
else:
    x = det_x/main_det
    y = det_y/main_det
    print(2, x, y)





