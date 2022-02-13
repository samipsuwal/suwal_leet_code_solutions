class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        aDict ={}
        
        
        for i in range(len(s)):
            if s[i] not in aDict.keys():
                aDict[s[i]] = i # key is the letter and value if the index
            else:
                aDict[s[i]] = -1 #flag duplicates with -1
        minIndex =-1
        
        for k in aDict.keys():
            if aDict[k] > minIndex:
                minIndex=aDict[k]
                break
                
                
        return minIndex
        