class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cans = []

        if n ==1 and nums[0]>=1:
            return True

        cans.append(n-1)

        for i in range(n-2, -1,-1):
            if nums[i]>= n-i-1:
                cans.append(i)
            elif nums[i] + i >= cans[len(cans)-1]:
                cans.append(i)

        if cans[len(cans)-1] == 0:
            return True
        else:
            return False
        
        