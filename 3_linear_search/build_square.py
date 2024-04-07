def read_coordinates():
    n = int(input())
    coordinates = []
    for i in range(n):
        coordinates.append(tuple(map(int, input().split())))
    return n, coordinates


def print_result(res, res_coords):
    print(res)
    for line in res_coords:
        print(*line)


def is_int(x):
    return (x // 2) * 2 == x


def get_res_coord_1_2(input_points, coord_1, coord_2):
    counter = 0
    result_coords = []
    if coord_1 not in input_points:
        counter += 1
        result_coords.append(coord_1)
    if coord_2 not in input_points:
        counter += 1
        result_coords.append(coord_2)
    return counter, result_coords


def circle_1(input_points, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x11 = x1 + dy
    y11 = y1 - dx
    x22 = x2 + dy
    y22 = y2 - dx
    return get_res_coord_1_2(input_points, coord_1=(x11, y11), coord_2=(x22, y22))


def circle_2(input_points, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x11 = x1 - dy
    y11 = y1 + dx
    x22 = x2 - dy
    y22 = y2 + dx
    return get_res_coord_1_2(input_points, coord_1=(x11, y11), coord_2=(x22, y22))


def circle_3(input_points, x1, y1, x2, y2):
    if x1 >= x2:
        x_l, y_l = x2, y2
        x_r, y_r = x1, y1
    else:
        x_l, y_l = x1, y1
        x_r, y_r = x2, y2

    sum_x = x1 + x2
    sum_y = y1 + y2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if y_r > y_l:
        x11_2 = sum_x - dy
        y11_2 = sum_y + dx

        x22_2 = sum_x + dy
        y22_2 = sum_y - dx
    else:
        x11_2 = sum_x - dy
        y11_2 = sum_y - dx

        x22_2 = sum_x + dy
        y22_2 = sum_y + dx

    is_all_correct = True
    for x in [x11_2, y11_2, x22_2, y22_2]:
        if not is_int(x):
            is_all_correct = False
            break
    if is_all_correct:
        return get_res_coord_1_2(input_points, coord_1=(x11_2 // 2, y11_2 // 2), coord_2=(x22_2 // 2, y22_2 // 2))
    return None, None


def count_dots_to_full_square():
    n, coordinates = read_coordinates()
    if n == 1:
        print('3_linear_search')
        x, y = list(coordinates)[0]
        print(x + 1, y)
        print(x + 1, y + 1)
        print(x, y + 1)
        return

    input_points = set(tuple(x) for x in coordinates)
    result = 4
    result_coords = []
    for i, (x1, y1) in enumerate(coordinates[:-1]):
        for j, (x2, y2) in enumerate(coordinates[i + 1:]):
            res_ij, result_ij = circle_1(input_points, x1, y1, x2, y2)
            if res_ij < result:
                result, result_coords = res_ij, result_ij

            res_ij, result_ij = circle_2(input_points, x1, y1, x2, y2)
            if res_ij < result:
                result, result_coords = res_ij, result_ij

            res_ij, result_ij = circle_3(input_points, x1, y1, x2, y2)
            if res_ij is not None and res_ij < result:
                result, result_coords = res_ij, result_ij

            if result == 0:
                print(result)
                return

    print_result(result, set(result_coords))
    return


count_dots_to_full_square()
