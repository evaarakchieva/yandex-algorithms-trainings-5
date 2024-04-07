n = int(input())
nums = list(map(int, input().split()))
frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_frequent_num = next(iter(frequency))
max_frequency = frequency[max_frequent_num]
for num, count in frequency.items():
    if num + 1 in frequency:
        count += frequency[num + 1]
    if count > max_frequency:
        max_frequency = count
        max_frequent_num = num

ans = sum(frequency[num] for num in frequency if num != max_frequent_num and num != max_frequent_num + 1)

print(ans)
