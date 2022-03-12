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
                cans.sort()
            elif nums[i] + i >= cans[0]:
                cans.append(i)
                cans.sort()


        print(cans)
        if cans[0] == 0:
            return True
        else:
            return False
        
        