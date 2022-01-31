class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        max_profit = 0

        if length == 1:
            return 0

        else: 
            for i in range(length):

                for j in range(i + 1, length):
                    num1 = prices[i]
                    num2 = prices[j]
                    profit = num2 - num1

                    if profit > max_profit:
                        max_profit = profit
                    
                
        return max_profit

    
