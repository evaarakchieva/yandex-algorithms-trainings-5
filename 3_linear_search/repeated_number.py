n, k = map(int, input().split())
numbers = list(map(int, input().split()))

reiteration = {}

for index, number in enumerate(numbers):
    if number not in reiteration:
        reiteration[number] = set()
    reiteration[number].add(index)

ans = "NO"
for indices in reiteration.values():
    indices = sorted(indices)
    if len(indices) > 1:
        min_diff = min(indices[i + 1] - indices[i] for i in range(len(indices) - 1))
        if min_diff <= k:
            ans = "YES"
            break

print(ans)
