P1_x, P1_y = map(int, input().split())
P2_x, P2_y = map(int, input().split())
P3_x, P3_y = map(int, input().split())

try:
    k = - ((P2_y - P1_y) / (P2_x - P1_x)) * P1_x + P1_y
except ZeroDivisionError:
    if (P2_y > P1_y and P3_x < P1_x) or (P2_y < P1_y and P1_x > P3_x):
        print(-1)
        exit()
    elif (P2_y > P1_y and P1_x < P3_x) or (P2_y < P1_y and P1_x < P3_x):
        print(1)
        exit()
    else:
        print(0)
        exit()
# 일직선
if ((P2_y - P1_y) / (P2_x - P1_x)) * P3_x + k == P3_y:
    print(0)

elif ((P2_y - P1_y) / (P2_x - P1_x)) * P3_x + k < P3_y:
    print(1)

else:
    print(-1)