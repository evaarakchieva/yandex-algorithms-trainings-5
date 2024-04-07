def count_max_profit(days, expiration, fish_prices):
    max_profit = 0
    for i in range(days):
        buy_price = fish_prices[i]
        for j in range(i + 1, min(i + expiration + 1, n)):
            sell_price = fish_prices[j]
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit
    return max_profit


n, k = map(int, input().split())
prices = list(map(int, input().split()))
print(count_max_profit(n, k, prices))
