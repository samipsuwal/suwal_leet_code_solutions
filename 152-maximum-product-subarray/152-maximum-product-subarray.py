class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
    
        maxi=mini=ans= nums[0]

        for i in range(1, n):
            candidates = [nums[i], mini*nums[i], maxi*nums[i]]
            mini = min(candidates)
            maxi = max(candidates)
            ans= max(maxi, ans)

        return ans
        
        