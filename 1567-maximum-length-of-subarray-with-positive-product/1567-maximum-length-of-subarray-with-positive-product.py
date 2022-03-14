class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        lastNegativeIndex = lastZeroIndex=-1
        best=[0]*n
        negs=0



        for i in range(n):
            x= nums[i]
            if x==0:
                #reset
                lastZeroIndex=i
                lastNegativeIndex=i
                negs=0
                continue
            if x<0:
                if negs==0:
                    lastNegativeIndex=i
                negs+=1


            if negs%2!=0:#odd
                best[i]= i-lastNegativeIndex
            else:#even
                best[i]= i- lastZeroIndex
        best.sort()    
        return best[-1]