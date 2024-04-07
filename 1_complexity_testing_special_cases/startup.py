def count_profit(n, k, d):
    for _ in range(d):
        is_found = False
        for digit in range(10):
            current_profit = n + str(digit)
            if int(current_profit) % k == 0:
                n = current_profit
                is_found = True
                break
        if not is_found:
            return -1
        else:
            return n + '0' * (d - 1)


input_n, input_k, input_d = map(int, input().split())
input_n = str(input_n)
print(count_profit(input_n, input_k, input_d))
