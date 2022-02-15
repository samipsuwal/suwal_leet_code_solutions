class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        def doesAnyKeyHasMoreThanOne(aDict):
            for i in aDict.keys():
                if aDict[i] >=2:
                    return True

            return False
        
        
        
        aDict= {}
        window=0
        continueWhileLoop = True
        maxCount = 0
        leftIndex = 0
        for a in s:
            if a not in aDict.keys():
                aDict[a] = 1
            else:
                aDict[a] +=1
            window+=1
            if doesAnyKeyHasMoreThanOne(aDict):
                while continueWhileLoop:
                    #print(aDict,a)
                    toRemove = s[leftIndex]
                    aDict[toRemove] = aDict[toRemove] -1
                    if aDict[toRemove] == 0:
                        aDict.pop(toRemove)

                    window -=1
                    leftIndex +=1
                    if not doesAnyKeyHasMoreThanOne(aDict):
                        continueWhileLoop = False

                continueWhileLoop = True
                #print(aDict,a,"After While")
            else: 
                maxCount = max(maxCount,window)


        return maxCount
