class Solution:
    def trap(self, height: List[int]) -> int:
        nums=height
        n= len(nums)
        leftMost=[0]*n
        rightMost = [0]*n
        waterFill =[0]*n

        leftMost[0]=nums[0]
        leftMostHeight=nums[0]
        rightMost[n-1] = nums[n-1]
        rightMostHeight=nums[n-1]

        for i in range(1, n):
            if nums[i]<leftMostHeight:
                leftMost[i]=leftMostHeight
            else:
                leftMost[i] = nums[i]
                leftMostHeight = nums[i]

        for i in range(n-2, -1,-1):
            if nums[i]<rightMostHeight:
                rightMost[i] =rightMostHeight
            else:
                rightMost[i] = nums[i]
                rightMostHeight = nums[i]


        trapWater =0
        for i in range(1, n-1):
            mini = min(leftMost[i], rightMost[i])
            maxi = max(leftMost[i], rightMost[i])
            if nums[i]<mini and nums[i] <maxi:
                trapWater += mini - nums[i]


        return trapWater
                    
        