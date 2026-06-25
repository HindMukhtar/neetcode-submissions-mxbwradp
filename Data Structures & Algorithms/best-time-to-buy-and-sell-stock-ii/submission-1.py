class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # profit - sell price - buy price 
        # we want max profit, i.e we want min buy price for every sell price 
        profit = 0 
        for i in range(1, len(prices)): 
            if prices[i] > prices[i-1]: 
                profit += prices[i] - prices[i-1]

        return profit