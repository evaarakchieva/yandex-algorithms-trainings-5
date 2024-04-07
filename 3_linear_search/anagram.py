a = list(input())
b = list(input())

a_dict = {}
b_dict = {}
for i in range(len(a)):
    if a[i] in a_dict:
        a_dict[a[i]] += 1
    else:
        a_dict[a[i]] = 1

    if b[i] in b_dict:
        b_dict[b[i]] += 1
    else:
        b_dict[b[i]] = 1

if a_dict == b_dict:
    print('YES')
else:
    print('NO')
