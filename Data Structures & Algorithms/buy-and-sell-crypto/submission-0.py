class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = 0
        days = len(prices)
        i=0
        lowest_price = prices[0]
        while(i+1 < days):
            lowest_price = min(lowest_price, prices[i+1])

            curr_profit = prices[i+1] - lowest_price
            max_profit = max(curr_profit, max_profit)

            i+=1
        
        if max_profit < 0:
            return 0
        else:   
            return max_profit
        