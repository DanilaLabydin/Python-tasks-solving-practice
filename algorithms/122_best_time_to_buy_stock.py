from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        day_buy = prices[0]
        for day_sell in prices[1:]:
            if day_sell > day_buy:
                max_profit += day_sell - day_buy
            day_buy = day_sell

        return max_profit


Test = Solution()
array1 = [7, 1, 5, 3, 6, 4]
array2 = [7, 6, 4, 3, 1]
array3 = [3, 3, 5, 0, 0, 3, 1, 4]

print(Test.maxProfit(array3))
