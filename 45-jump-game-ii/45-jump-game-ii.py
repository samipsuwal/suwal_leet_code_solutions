class Solution:
    def jump(self, nums: List[int]) -> int:
    
        def helper(idx, nums, memo):

            if idx >= len(nums)-1:
                return 0
            if nums[idx]==0:
                return None

            if idx in memo:
                return memo[idx]

            shortestNumberOfJumps = None

            jumps = nums[idx]
            while jumps>0:
                steps = helper(idx+jumps, nums, memo)

                if steps!= None:
                    steps+=1
                    if shortestNumberOfJumps == None or shortestNumberOfJumps > steps:
                        shortestNumberOfJumps = steps
                jumps-=1

            if shortestNumberOfJumps!=None:
                memo[idx] = shortestNumberOfJumps  
            else:
                memo[idx] =None
            return memo[idx]

        return helper(0, nums,{})
    
    
    
        

