def determine_height(width, array):
    height, l = 0, 0
    for i in array:
        if l != 0:
            if l + i <= width - 1:
                l += i + 1
            else:
                l = i
                height += 1
        elif i < width:
            l = i
            height += 1
        elif i == width:
            height += 1
            l = 0
    return height


def determine_opt_width(h, array):
    width_range = range(max(array), sum(array) + len(array) + 1)
    left, right = 0, len(width_range) - 1
    ind = -1
    while left <= right:
        mid = (left + right) // 2
        if determine_height(width_range[mid], array) <= h:
            ind = mid
            right = mid - 1
        else:
            left = mid + 1
    if ind != -1:
        opt = width_range[ind]
        return opt


def determine_min_width(h, array_1, array_2):
    width_1 = determine_opt_width(h, array_1)
    width_2 = determine_opt_width(h, array_2)
    w_sum = width_1 + width_2
    return w_sum, max(determine_height(width_1, array_1), determine_height(width_2, array_2))


def solve():
    w, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    h_range = range(1, n + m + 1)
    left, right = 0, len(h_range) - 1
    solution = -1
    while left <= right:
        mid = (left + right) // 2
        w_min, h_opt = determine_min_width(h_range[mid], a, b)
        if w_min > w:
            left = mid + 1
        else:
            solution = h_opt
            right = mid - 1
    if solution != -1:
        print(solution)


solve()
