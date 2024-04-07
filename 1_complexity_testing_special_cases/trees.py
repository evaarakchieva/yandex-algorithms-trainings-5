p, v = map(int, input().split())
q, m = map(int, input().split())

ans = 0
if p - v >= q - m and p + v <= q + m:  # (p-v,p+v) is fully in (q-m,q+m)
    ans = 2 * m + 1
elif q - m >= p - v and q + m <= p + v:  # (q-m,q+m) is fully in (p-v,p+v)
    ans = 2 * v + 1
elif p > q:
    if p - v > q + m:
        ans = 2 * v + 2 * m + 2
    elif p - v < q + m:
        ans = 2 * v + 2 * m + 2 - (q + m - (p - v)) - 1
    else:
        ans = 2 * v + 2 * m + 2 - 1
elif p < q:
    if q - m > p + v:
        ans = 2 * v + 2 * m + 2
    elif q - m < p + v:
        ans = 2 * v + 2 * m + 2 - (p + v - (q - m)) - 1
    else:
        ans = 2 * v + 2 * m + 2 - 1
else:
    if v >= m:
        ans = 2 * v + 1
    else:
        ans = 2 * m + 1

print(ans)

