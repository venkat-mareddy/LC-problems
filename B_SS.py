def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #bruteforce solution
        """
        n = len(prices)

        profit = 0
        for i in range(0, n-1):
            for j in range(i+1, n):
                if(prices[i] < prices[j]):
                    temp = prices[j] - prices[i]
                if(temp > profit):
                    profit = temp
        return profit
	"""
        #other solution
        if len(prices) == 0: 
            return 0        
        else:
            low = 99999 
            profitmax = 0
            for price in prices:
                if price > low:
                    if price - low > profitmax:
                        profitmax = price - low                        
                elif price < low:
                    low = price
                
            return profitmax

p = maxProfit([2, 4, 1])
print("Profit")
print(p)
