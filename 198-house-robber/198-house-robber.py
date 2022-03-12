class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n ==1:
            return nums[0]
        
        costs = [0]*n
        
        costs[0] = nums[0]
        costs[1] = max(nums[0], nums[1])
        
        for i in range(2,n):
            costs[i] = max(nums[i] + costs[i-2], costs[i-1])
            
        return costs[n-1]
            