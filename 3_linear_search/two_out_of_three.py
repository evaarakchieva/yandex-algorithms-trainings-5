size_1 = int(input())
list_1 = list(map(int, input().split()))
size_2 = int(input())
list_2 = list(map(int, input().split()))
size_3 = int(input())
list_3 = list(map(int, input().split()))

result = set()
for i in list_1:
    if i in list_2 or i in list_3:
        result.add(i)

for i in list_2:
    if i in list_1 or i in list_3:
        result.add(i)

for i in list_3:
    if i in list_1 or i in list_2:
        result.add(i)

result = sorted(result)

print(' '.join(map(str, result)))
