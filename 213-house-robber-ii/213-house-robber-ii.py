import copy
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        if len(nums) ==2:
            return max(nums[0], nums[1])
        
        if len(nums) ==3:
            return max(nums[0], nums[1], nums[2])
        
        s_nums = copy.deepcopy(nums)
        
        # last taken out
        s_nums.pop()
        #first taken out
        nums.pop(0)
        
        n = len(nums)
        
        costs=[0]*n
        s_costs=[0]*n
        
        costs[0] = nums[0]
        s_costs[0]= s_nums[0]
        
        costs[1] = max(nums[0], nums[1])
        s_costs[1]= max(s_nums[0], s_nums[1])
        
        
        for i in range(2,n):
            costs[i] = max(nums[i]+costs[i-2], costs[i-1])
            s_costs[i] = max(s_nums[i]+s_costs[i-2], s_costs[i-1])
            
        return max(s_costs[n-1], costs[n-1])
        
        
        
        
        
        
        
        
                
        
        
        
            
        
        