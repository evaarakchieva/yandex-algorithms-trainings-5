def bin_search(data, x, y, left, right):
    res = -1
    while left < right:
        mid = (left + right) // 2
        now_sum = data[mid] - data[mid - y]
        if now_sum == x:
            res = mid - y + 1
            break
        elif now_sum >= x:
            right = mid
        else:
            left = mid + 1
    return res


n, m = map(int, input().split())
orcs_per_regiment = list(map(int, input().split()))
requests = []
for _ in range(m):
    request = list(map(int, input().split()))
    requests.append(request)

prefix_sums = [0]
for i in range(n):
    prefix_sums.append(prefix_sums[i] + orcs_per_regiment[i])

for request in requests:
    regiment = request[0]
    orcs = request[1]
    l = regiment
    r = n + 1
    print(bin_search(prefix_sums, orcs, regiment, l, r))
