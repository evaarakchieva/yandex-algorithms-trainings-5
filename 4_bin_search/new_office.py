def count_sum(l_x, l_y, r_x, r_y, mtrx):
    return mtrx[r_x][r_y] + mtrx[l_x][l_y] - mtrx[r_x][l_y] - mtrx[l_x][r_y]


def count_cells(x, y, k, matrix):
    ctr = count_sum(x, y + k, x + 3 * k, y + 2 * k, matrix)
    left = count_sum(x + k, y, x + 2 * k, y + k, matrix)
    right = count_sum(x + k, y + 2 * k, x + 2 * k, y + 3 * k, matrix)
    return ctr + left + right


def check_func(matrix, k, n, m):
    for x in range(n - 3 * k + 1):
        for y in range(m - 3 * k + 1):
            if count_cells(x, y, k, matrix) == 5 * k * k:
                return 1
    return 0


def bin_search(left, right, matrix, n, m):
    while left < right:
        mid = (left + right + 1) // 2
        if check_func(matrix, mid, n, m):
            left = mid
        else:
            right = mid - 1
    return left


def count_prefix_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for j in range(cols):
        for i in range(rows):
            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + matrix[i][j]
    return prefix_sum


def solve():
    n, m = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        row = input()
        for j in range(m):
            if row[j] == '#':
                matrix[i][j] = 1
    prefix_sum = count_prefix_sum(matrix)
    print(bin_search(1, min(n, m) // 3, prefix_sum, n, m))


solve()
