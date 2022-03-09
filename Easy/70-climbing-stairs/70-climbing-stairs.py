class Solution:
    def climbStairs(self, n: int) -> int:
        
        hm = {}
        hm[1]=1
        hm[2] = 2
        for i in range(3, n+1):
            hm[i] = hm[i-1] + hm[i-2]
            
        return hm[n]
        