def count_sectors(speed, slowdown):
    if speed % slowdown == 0:
        sectors = speed // slowdown - 1
    else:
        sectors = speed // slowdown
    return sectors


def count_biggest_prize(n, prizes, a, b, k):
    max_prize = -1
    min_s = count_sectors(a, k)
    max_s = count_sectors(b, k)
    if max_s - min_s >= len(prizes):
        return max(prizes)
    else:
        for v in range(min_s, max_s + 1):
            max_prize = max(max_prize, prizes[v % n], prizes[(n - (v % n)) % n])
    return max_prize


input_n = int(input())
input_prizes = list(map(int, input().split()))
input_a, input_b, input_k = map(int, input().split())

print(count_biggest_prize(input_n, input_prizes, input_a, input_b, input_k))
