n = int(input())
numbers = list(map(int, input().split()))

if n == 2:
    if numbers[0] % 2 != 0 and numbers[1] % 2 != 0:
        print('x')
    else:
        print('+')
elif numbers[-1] % 2 != 0:
    ans = '+' * (n - 2)
    summa = 0
    for i in range(n - 1):
        summa += numbers[i]
    if summa % 2 == 0:
        ans += '+'
    else:
        ans += 'x'
    print(ans)
else:
    ans = ['_'] * (n - 1)
    ans[-1] = '+'
    i = -2
    while i > -n-1:
        if numbers[i] % 2 == 0:
            ans[i] = '+'
        else:
            summa = 0
            for j in range(-n, i, 1):
                summa += numbers[j]
                ans[j+1] = '+'
            if summa % 2 == 0:
                ans[i] = '+'
            else:
                ans[i] = 'x'
            break
        i -= 1
    print(''.join(ans))
