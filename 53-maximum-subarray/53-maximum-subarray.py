class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n= len(nums)
        best=[0]*n
        
        if n ==1:
            return nums[0]
        
        best[n-1] = nums[n-1]
        
        for i in  reversed(range(len(nums)-1)):
            best[i] = max(nums[i], nums[i]+best[i+1])
            
        maxi=best[0]
        
        for i in best:
            maxi = max(maxi, i)
            
        return maxi
            