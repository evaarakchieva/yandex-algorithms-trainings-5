def move_all_to_one_column(ships, n):
    move_all_to_column = {}
    
    for col in range(1, n + 1):
        moves = 0
        for ship in ships:
            moves += abs(ship[1] - col)
        move_all_to_column[col] = moves

    right_left_moves = min(move_all_to_column.values())
    column_with_min_moves_x = min([key for key, value in move_all_to_column.items() if value == right_left_moves])

    up_down_moves_made = 0
    current_ship = []
    ships_to_move_up_down = ships.copy()
    ships_to_move_up_down.sort()
    free_cells = [(i, column_with_min_moves_x) for i in range(1, n + 1)]
    free_cells.sort()

    for cell in free_cells:
        min_ship = []

        if current_ship:
            for ship in current_ship:
                dist = abs(cell[0] - ship[0])
                min_ship.append(dist)

            min_moves_for_ship = min(min_ship)
            min_moves_index = min_ship.index(min_moves_for_ship)
            up_down_moves_made += min_moves_for_ship
            current_ship.pop(min_moves_index)
            ships_to_move_up_down.pop(min_moves_index)

        else:
            for ship in ships_to_move_up_down:
                dist = abs(cell[0] - ship[0])
                min_ship.append(dist)

            min_moves_for_ship = min(min_ship)
            up_down_moves_made += min_moves_for_ship
            min_moves_index = min_ship.index(min_moves_for_ship)
            ships_to_move_up_down.pop(min_moves_index)

        for i in ships_to_move_up_down:
            if i[0] == cell[0]:
                current_ship.append(i)

    total_moves = right_left_moves + up_down_moves_made
    return total_moves
    

input_n = int(input())
input_ships = []
for _ in range(input_n):
    coords = list(map(int, input().split()))
    input_ships.append(coords)

ans = move_all_to_one_column(input_ships, input_n)
print(ans)

# from statistics import median
#
# n = int(input())
#
# # Сохраним по отдельности массивы с координатами по гориз. и вертикали
# y_coords = []
# x_coords = []
# for _ in range(n):
#     coord = list(map(int, input().split()))
#     x_coords.append(coord[1_complexity_testing_special_cases] - 1_complexity_testing_special_cases)
#     y_coords.append(coord[0] - 1_complexity_testing_special_cases)
#
# y_moves = 0
#
# # Для начала разберемся с "вертикальными" ходами:
# # каждый корабль должен встать в ту строку, к которой он ближе
# y_coords.sort()
# for i, y in enumerate(y_coords):
#     y_moves += abs(i - y)
#
# # Теперь посчитаем минимум для "горизонтальных" ходов.
# # Оптимальным столбцом является медиана
# median_col = round(median(x_coords))
# x_moves = sum([abs(x - median_col) for x in x_coords])
#
# print(x_moves + y_moves)