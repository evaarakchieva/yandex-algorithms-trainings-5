def generate_vector(coordinates):
    x1, y1, x2, y2 = coordinates
    start_x, start_y = x1, y1
    end_x, end_y = x2, y2
    if (start_y == end_y and start_x > end_x) or start_y > end_y:
        start_x, start_y = x2, y2
        end_x, end_y = x1, y1
    dx, dy = end_x - start_x, end_y - start_y
    return (start_x, start_y), (dx, dy)


def generate_direction(image):
    direction = {(move_x, move_y): [] for coordinates in image for (start_x, start_y), (move_x, move_y) in [generate_vector(coordinates)]}
    for coordinates in image:
        (start_x, start_y), (move_x, move_y) = generate_vector(coordinates)
        direction[(move_x, move_y)].append((start_x, start_y))
    return direction


def find_solution():
    n = int(input())
    image_a = [list(map(int, input().split())) for _ in range(n)]
    image_b = [list(map(int, input().split())) for _ in range(n)]
    direction_a = generate_direction(image_a)
    direction_b = generate_direction(image_b)
    difference = dict()
    count_match = 0
    for key, value in direction_b.items():
        if key in direction_a:
            for (x1, y1) in value:
                for (x2, y2) in direction_a[key]:
                    dx, dy = x2 - x1, y2 - y1
                    difference[(dx, dy)] = difference.get((dx, dy), 0) + 1
                    count_match = max(count_match, difference[(dx, dy)])
    print(n - count_match)


find_solution()
