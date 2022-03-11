class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        min_val = prices[0]
        max_profit = 0

        if length == 1:
            return 0

        else: 
            for i in range(length):
                if prices[i] < min_val:
                    min_val = prices[i]
                
                profit = prices[i] - min_val

                if profit > max_profit:
                    max_profit = profit
                    
                
        return max_profit

    
