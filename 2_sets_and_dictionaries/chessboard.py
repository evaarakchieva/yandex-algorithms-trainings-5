def count_figure_perimeter(coordinates):
    cells = set(tuple(coordinate) for coordinate in coordinates)
    perimeter = 0
    for x, y in cells:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x + dx, y + dy) not in cells:
                perimeter += 1
    return perimeter


n = int(input())
input_list = []
for i in range(n):
    input_list.append(list(map(int, input().split())))

ans = count_figure_perimeter(input_list)
print(ans)
