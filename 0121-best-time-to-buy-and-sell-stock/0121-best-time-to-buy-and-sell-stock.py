class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_price = 2 ** 31 - 1
        
        for i in range(len(prices)):
            
            max_profit = max(max_profit, prices[i] - min_price)
            
            if prices[i] < min_price:
                min_price = prices[i]
            
        return max_profit
        