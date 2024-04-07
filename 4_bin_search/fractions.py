n = int(input())
left, right = 1, n

while left < right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 < n:
        left = mid + 1
    else:
        right = mid

diag = right
first_number = (diag - 1) * diag // 2 + 1
distance = n - first_number

if diag % 2 == 0:
    print(f'{diag - distance}/{1 + distance}')
else:
    print(f'{1 + distance}/{diag - distance}')
