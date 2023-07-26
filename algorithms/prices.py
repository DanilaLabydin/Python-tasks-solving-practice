def calculate_optimal_transactions(prices):
    n = len(prices)
    buy_day, sell_day = [], []
    buy_index = -1  # Index of the potential buy day
    max_profit = 0  # Maximum profit achieved
    k = 0  # Number of pairs of transactions

    # Find the potential buy and sell days
    for i in range(n - 1):
        if prices[i] < prices[i + 1]:
            if buy_index == -1:
                buy_index = i
            sell_index = i + 1
            profit = prices[sell_index] - prices[buy_index]

            if profit > max_profit:
                max_profit = profit
                buy_day = [buy_index + 1]
                sell_day = [sell_index + 1]
                k = 1

    # Check if additional transactions can improve the profit
    while k < 2 and buy_day:
        # Remove the first pair of transactions from the prices
        prices = prices[sell_day[0] :]
        n = len(prices)
        buy_index = -1

        # Find the potential buy and sell days in the updated prices
        for i in range(n - 1):
            if prices[i] < prices[i + 1]:
                if buy_index == -1:
                    buy_index = i
                sell_index = i + 1
                profit = prices[sell_index] - prices[buy_index]

                if profit > max_profit:
                    max_profit = profit
                    buy_day.append(buy_index + sell_day[0] + 1)
                    sell_day.append(sell_index + sell_day[0] + 1)
                    k = 2

    return k, buy_day, sell_day


# Read the input
n = int(input())
prices = list(map(int, input().split()))

# Calculate the optimal transactions
k, buy_day, sell_day = calculate_optimal_transactions(prices)

# Print the result
print(k)
for i in range(k):
    print(buy_day[i], sell_day[i])
