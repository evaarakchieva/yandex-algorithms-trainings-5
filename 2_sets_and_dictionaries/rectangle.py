k = int(input())
min_x, min_y = map(int, input().split())
max_x = min_x
max_y = min_y
for _ in range(k - 1):
    now_x, now_y = map(int, input().split())
    if now_x < min_x:
        min_x = now_x
    if now_x > max_x:
        max_x = now_x
    if now_y < min_y:
        min_y = now_y
    if now_y > max_y:
        max_y = now_y
print(min_x, min_y, max_x, max_y)
