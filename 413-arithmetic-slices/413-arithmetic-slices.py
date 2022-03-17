class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n<3:
            return 0
        
        diffs = [0]*(n-1)
        
        for i in range(n-1):
            diffs[i] = nums[i+1]-nums[i]
            
        print(diffs)
        
        #if two diffs are a match, we have atleast 1
        ans=0
        for i in range(n-2):
            j =i+1
            if diffs[j] == diffs[i]:
                ans+=1
                j+=1
                while j< n-1:
                    if diffs[j]== diffs[i]:
                        ans+=1
                    else:
                        break
                    j+=1
                        
        return ans