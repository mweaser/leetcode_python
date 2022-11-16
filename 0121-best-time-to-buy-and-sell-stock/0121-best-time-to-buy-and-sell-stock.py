class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = 2 ** 31 - 1
        max_sum = 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                
            max_sum = max(max_sum, prices[i] - min_price)
        
        return max_sum