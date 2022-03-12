class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
         
        def helper(nums, i, target, memo):
            if target==0 and i == len(nums):
                return 1

            if i>= len(nums):
                return 0

            if (i,target) in memo:
                return memo[i,target]

            add =  helper(nums, i+1, target-nums[i], memo)
            substract = helper(nums, i+1, target+nums[i], memo)

            memo[i,target] =  add+ substract

            return memo[i,target]


        return helper(nums, 0, target,{})