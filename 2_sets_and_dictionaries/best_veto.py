def find_max(forces, row_to_exclude, column_to_exclude):
    flag = True
    max_force = max_row = max_column = 0
    for i, row in enumerate(forces):
        if i == row_to_exclude:
            continue
        for j, force in enumerate(row):
            if j == column_to_exclude:
                continue
            if flag or force > max_force:
                max_force = force
                max_row = i
                max_column = j
                flag = False
    return max_force, max_row, max_column


def ban(forces):
    global_max_force, i_max_force, j_max_force = find_max(forces, -1, -1)

    # row -> column
    max_force_without_row, i, j = find_max(forces, i_max_force, -1)
    max_force_without_row_column, _, _ = find_max(forces, i_max_force, j)

    # column -> row
    max_force_without_column, i, _ = find_max(forces, -1, j_max_force)
    max_force_without_column_row, _, _ = find_max(forces, i, j_max_force)

    if max_force_without_row_column < max_force_without_column_row:
        result_row = i_max_force
        result_column = j
    else:
        result_row = i
        result_column = j_max_force

    return result_row + 1, result_column + 1


input_n, input_m = map(int, input().split())
input_forces = [list(map(int, input().split())) for _ in range(input_n)]
print(' '.join(map(str, ban(input_forces))))
