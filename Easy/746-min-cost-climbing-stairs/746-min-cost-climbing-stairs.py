class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        b=[0]*n
        
        
        #b[0]=cost[0]
        
        
        for i in range (n):
            if i < n-1:
                b[i] = min(cost[i]+b[i-1],cost[i]+b[i-2])
            else:
                b[i] = min(b[i-1],cost[i]+b[i-2])
        
        print(b)
        
        return b[n-1]