class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        i =0
        j = len(nums)-1
        
        ans =-1
        
        while i!=j:
            if nums[i] + nums[j] >= k:
                j-=1
            elif nums[i] + nums[j] < k:
                ans = max(ans, nums[i]+nums[j])
                i+=1
                
        return ans
            
                
        