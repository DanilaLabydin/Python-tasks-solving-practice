from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy_price_log = []
        for index_buy in range(len(prices)):
            buy_price = prices[index_buy]
            if buy_price in buy_price_log:
                continue

            buy_price_log.append(buy_price)
            max_sell_price = max(prices[index_buy:])
            if max_sell_price < buy_price:
                continue

            profit = max_sell_price - buy_price
            if profit > best:
                best = profit

            # for sell_price in set(prices[index_buy + 1:]):
            #     profit = sell_price - prices[index_buy]
            #     # print(f'buy: {prices[index_buy]} -- sell: {prices[index_sell]} -- profit: {profit}')
            #     if profit > best:
            #         best = profit

        return best


Test = Solution()
array1 = [7, 1, 5, 3, 6, 4]
array2 = [7, 6, 4, 3, 1]
print(Test.maxProfit(array2))
