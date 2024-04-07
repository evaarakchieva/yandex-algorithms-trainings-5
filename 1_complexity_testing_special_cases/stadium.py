def count_time(length, x1, v1, x2, v2):
    x1 = x1 % length
    x2 = x2 % length
    t = 0

    if x1 > x2:
        x1, x2 = x2, x1
        v1, v2 = v2, v1

    is_possible = True
    if x1 != x2 and v1 + v2 != 0:
        time_1 = 0
        time_2 = 0
        count_circles = 0

        while time_1 <= 0 and time_2 <= 0:
            time_1 = (count_circles * length - (x1 + x2) % length) / (v1 + v2)
            time_2 = (-count_circles * length - (x1 + x2) % length) / (v1 + v2)
            count_circles += 1
        else:
            if time_1 * time_2 < 0:
                t = max(time_1, time_2)
            else:
                t = min(time_1, time_2)
    else:
        if (x1 + x2) % length == 0 or (x1 - x2) % length == 0 or x1 == x2:
            t = 0
        elif v1 == -v2 and v1 == 0:
            is_possible = False
        elif v1 < 0:
            t = (length - x2 + x1) / (v2 - v1)
        else:
            t = (x2 - x1) / (v1 - v2)

    if v1 != v2 and is_possible:
        time_3 = 0
        time_4 = 0
        count_circles = 0
        while time_3 <= 0 and time_4 <= 0:
            time_3 = (count_circles * length - (x1 - x2)) / (v1 - v2)
            time_4 = (-count_circles * length - (x1 - x2)) / (v1 - v2)
            count_circles += 1
        else:
            if time_3 * time_4 < 0:
                t = min((max(time_3, time_4)), t)
            else:
                t = min(min(time_3, time_4), t)

    if is_possible:
        print('YES')
        print(t)
    else:
        print('NO')

    return


input_l, input_x1, input_v1, input_x2, input_v2 = map(int, input().split())
count_time(input_l, input_x1, input_v1, input_x2, input_v2)
