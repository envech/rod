def max_profit_rod_cutting(n, prices):
    max_profit = [0] * (n + 1)
    lengths_used = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        max_value = -float('inf')
        for j in range(1, i + 1):
            current_value = prices[j - 1] + max_profit[i - j]
            if current_value > max_value:
                max_value = current_value
                lengths_used[i] = lengths_used[i - j] + [j]
        max_profit[i] = max_value

    return max_profit[n], lengths_used[n]

n = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]
max_value, lengths = max_profit_rod_cutting(n, prices)
print(f"Maximum profit: {max_value}")
print(f"Recommended lengths to cut: {lengths}")
