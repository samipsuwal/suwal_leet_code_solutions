class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==1:
            return 0
        
        buyPrice = prices[0]
        profit=0
        for i in range(1, n):
            
            if prices[i]<buyPrice:
                buyPrice = prices[i]
                continue
            
            if prices[i]> buyPrice and prices[i] -buyPrice > profit:
                profit= prices[i]-buyPrice
                    
        return profit
                
        