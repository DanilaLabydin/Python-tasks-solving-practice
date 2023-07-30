from typing import List


class Solution:
    def get_max_profit(self, prices: List[int]) -> int:
        best = 0
        day_buy = prices[0]
        for day_sell in prices[1:]:
            if day_sell > day_buy:
                best = max(best, day_sell - day_buy)
            else:
                day_buy = day_sell
        return best


    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        day_buy = 0
        for i in range(len(prices)):
            if prices[i] > prices[day_buy]:

                while i < len
                first_deal_profit = prices[i] - prices[day_buy]
                second_deal_profit = self.get_max_profit(prices[i:])

                best = max(best, first_deal_profit + second_deal_profit)
            else:
                day_buy = i
             
        return best

Test = Solution()
array1 = [7, 1, 5, 3, 6, 4]
array2 = [7, 6, 4, 3, 1]
print(Test.maxProfit(array2))

+79602551601 - Рома