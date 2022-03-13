class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==1:#according to test cases
            return 0

        bestWays = [0]*n
        bestWays[n-1]=1

        counter =3
        if n==2:
            counter=2

        for i in range(n-2, -1,-1):
            if nums[i]==0:
                continue
            elif nums[i]>= n-i-1:
                bestWays[i]=1
            else:
                candidates=[]
                jump=nums[i]
                while jump>0:
                    if bestWays[i+jump]>0:
                        candidates.append(bestWays[i+jump])

                    jump-=1
                if len(candidates)>0:
                    candidates.sort()
                    bestWays[i]= candidates[0]+1
        print(bestWays)
        return bestWays[0]

