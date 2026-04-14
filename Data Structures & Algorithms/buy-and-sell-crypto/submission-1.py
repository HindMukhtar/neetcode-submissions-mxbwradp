class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bestbuy = float('inf') 
        profit = 0 
        for i in range(1,n): 
            bestbuy = min(prices[i-1], bestbuy)
            profit = max(profit, prices[i] - bestbuy)
        
        return profit