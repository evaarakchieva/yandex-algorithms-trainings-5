chessboard = [list(input().strip()) for _ in range(8)]
under_attack = [['*' for _ in range(8)] for _ in range(8)]

figures = ['R', 'B']

for row in range(8):
    for col in range(8):
        if chessboard[row][col] != '*':
            under_attack[row][col] = chessboard[row][col]

for row in range(8):
    for col in range(8):
        if under_attack[row][col] == 'R':
            for r in range(row - 1, -1, -1):
                if under_attack[r][col] in figures:
                    break
                under_attack[r][col] = '0'
            for r in range(row + 1, 8):
                if under_attack[r][col] in figures:
                    break
                under_attack[r][col] = '0'
            for c in range(col - 1, -1, -1):
                if under_attack[row][c] in figures:
                    break
                under_attack[row][c] = '0'
            for c in range(col + 1, 8):
                if under_attack[row][c] in figures:
                    break
                under_attack[row][c] = '0'
        if under_attack[row][col] == 'B':
            for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if under_attack[r][c] in figures:
                    break
                under_attack[r][c] = '0'
            for r, c in zip(range(row + 1, 8), range(col - 1, -1, -1)):
                if under_attack[r][c] in figures:
                    break
                under_attack[r][c] = '0'
            for r, c in zip(range(row + 1, 8), range(col + 1, 8)):
                if under_attack[r][c] in figures:
                    break
                under_attack[r][c] = '0'
            for r, c in zip(range(row - 1, -1, -1), range(col + 1, 8)):
                if under_attack[r][c] in figures:
                    break
                under_attack[r][c] = '0'


safe_cells = sum(row.count('*') for row in under_attack)
print(safe_cells)
# print under_attack as matrix
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in under_attack]))
