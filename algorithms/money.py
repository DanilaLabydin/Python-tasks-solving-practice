def find_optimal_trading_days(N, prices):
    max_profit = 0
    buy_days = []
    sell_days = []

    # Find the best buy and sell days for a single transaction
    def find_single_transaction():
        buy_day, sell_day = 0, 0
        min_price = prices[0]
        max_profit = 0

        for i in range(1, N):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                buy_day = i
                sell_day = i

        return buy_day, sell_day

    # Find the best buy and sell days for two transactions
    def find_two_transactions():
        # Calculate the profit for the first transaction
        first_buy_day, first_sell_day = find_single_transaction()

        # Find the best second transaction after the first sell day
        max_profit = 0
        second_buy_day, second_sell_day = 0, 0

        for i in range(first_sell_day + 1, N):
            if prices[i] - prices[first_sell_day] > max_profit:
                max_profit = prices[i] - prices[first_sell_day]
                second_buy_day = i
                second_sell_day = i

        return (
            max_profit,
            first_buy_day,
            first_sell_day,
            second_buy_day,
            second_sell_day,
        )

    if N < 4:
        # Not enough data to perform two transactions
        max_profit, buy_day, sell_day = find_single_transaction()
        if max_profit > 0:
            buy_days.append(buy_day + 1)
            sell_days.append(sell_day + 1)
    else:
        # Perform two transactions
        (
            max_profit,
            first_buy_day,
            first_sell_day,
            second_buy_day,
            second_sell_day,
        ) = find_two_transactions()
        if max_profit > 0:
            buy_days.extend([first_buy_day + 1, second_buy_day + 1])
            sell_days.extend([first_sell_day + 1, second_sell_day + 1])

    return buy_days, sell_days


# Read input
N = int(input())
prices = list(map(int, input().split()))

# Calculate optimal trading days
buy_days, sell_days = find_optimal_trading_days(N, prices)

# Print the results
K = len(buy_days)
print(K)
for i in range(K):
    print(buy_days[i], sell_days[i])
