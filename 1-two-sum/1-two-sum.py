class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #redoing this for O(n)
        #traverse through this setup a hashmap

        aDict = {}
        for i in range(len(nums)):
            if nums[i] not in aDict:
                aDict[nums[i]] = [i]
            else:
                aDict[nums[i]].append(i)

        print(aDict)
        for i in aDict.keys():
                if target-i in aDict.keys():
                    if target-i !=i:
                        return [aDict[i][0], aDict[target-i][0]]

                    if (target-i == i) and len(aDict[i]) >=2:
                        return [aDict[i][0], aDict[target-i][1]]

        #will never hit since answer is guaranteed
        return 0
                      
        