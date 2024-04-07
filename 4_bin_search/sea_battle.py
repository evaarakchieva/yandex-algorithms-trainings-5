def check(n, mid):
    size = mid
    ships = 1
    total_ships = 0
    occupied_cells = 0
    while size > 0:
        occupied_cells += size * ships
        total_ships += ships
        if occupied_cells > n:
            return False
        ships += 1
        size -= 1
    occupied_cells += (total_ships - 1)
    return occupied_cells <= n


def bin_search(n):
    left, right = 0, n
    while left < right:
        mid = (left + right + 1) // 2
        if check(n, mid):
            left = mid
        else:
            right = mid - 1
    return left


n_cells = int(input())
print(bin_search(n_cells))
