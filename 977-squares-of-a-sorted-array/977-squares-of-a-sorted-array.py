class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        left =0
        right = n-1

        ans=[0]*n

        for i in range(n-1,-1,-1):
            if nums[left]**2 > nums[right]**2:
                ans[i] = nums[left]**2
                left+=1
            else:
                ans[i] = nums[right]**2
                right -=1

        return ans