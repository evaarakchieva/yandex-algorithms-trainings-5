def get_input():
    m, n = list(map(int, input().split()))
    grid = [input() for _ in range(m)]
    return m, n, grid


def get_hash_info(grid, m, n):
    hash_total = 0
    first_hash_row = -1
    last_hash_row = -1
    min_hash_col = float('inf')
    max_hash_col = -1

    for i in range(m):
        line = grid[i]
        hash_count = line.count('#')
        if hash_count > 0:
            hash_total += hash_count
            first_hash_row = i if first_hash_row == -1 else first_hash_row
            min_hash_col = min(min_hash_col, line.index('#'))
            max_hash_col = max(max_hash_col, line.rindex('#'))
            last_hash_row = i

    return hash_total, first_hash_row, min_hash_col, max_hash_col, last_hash_row


def process_grid(grid, hash_total, first_hash_row, n, m):
    if hash_total <= 1:
        return

    grid_copy = grid.copy()
    checked_hashes = 0
    line = grid_copy[first_hash_row]
    left = line.find('#')
    right = line.find('.', left)

    if right == -1:
        right = n

    temp = line[left: right]
    len_temp = right - left
    grid_copy[first_hash_row] = line[:left] + 'a' * len_temp + line[right:]
    checked_hashes += len_temp

    if checked_hashes == hash_total:
        grid_copy[first_hash_row] = grid_copy[first_hash_row].replace('a', 'b', 1)
        return grid_copy

    for i, line in enumerate(grid_copy[first_hash_row + 1:]):
        if line[left: right] == temp:
            grid_copy[first_hash_row + i + 1] = line[:left] + 'a' * len_temp + line[right:]
            checked_hashes += len_temp
        else:
            break

    if checked_hashes == hash_total:
        grid_copy[first_hash_row] = grid_copy[first_hash_row].replace('a', 'b')
        return grid_copy

    j = first_hash_row
    while '#' not in grid_copy[j]:
        j += 1

    line = grid_copy[j]
    left = line.find('#')

    right_dot = line.find('.', left)

    if right_dot == -1:
        right_dot = n

    right_a = line.find('a', left)

    if right_a == -1:
        right_a = n

    right = min(right_a, right_dot)
    temp = line[left: right]
    len_temp = right - left
    grid_copy[j] = line[:left] + 'b' * len_temp + line[right:]
    checked_hashes += len_temp

    for i, line in enumerate(grid_copy[j + 1:]):
        if line[left:right] == temp:
            grid_copy[j + i + 1] = line[:left] + 'b' * len_temp + line[right:]
            checked_hashes += len_temp
        else:
            break

    if checked_hashes == hash_total:
        return grid_copy
    return


m, n, grid = get_input()
hash_total, first_hash_row, min_hash_col, max_hash_col, last_hash_row = get_hash_info(grid, m, n)
result = process_grid(grid, hash_total, first_hash_row, n, m)

if not result:
    result = process_grid(list(map(''.join, (zip(*grid)))), hash_total, min_hash_col, m, n)
    if result:
        print('YES')
        print(*list(map(''.join, (zip(*result)))), sep='\n')
    else:
        print('NO')
else:
    print('YES')
    print(*result, sep='\n')
