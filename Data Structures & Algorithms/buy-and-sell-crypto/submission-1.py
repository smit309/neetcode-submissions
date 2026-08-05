class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0 

        [10,1,5,6,7,1]

        for price in range(len(prices)):
            if prices[price] < min_price:
                min_price = prices[price]
            elif prices[price] > min_price:
                if prices[price] - min_price > max_profit:
                    max_profit = prices[price] - min_price
            else: 
                continue        

        return max_profit            