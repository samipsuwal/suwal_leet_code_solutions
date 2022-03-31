class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        dict={}
        
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        
        reversedDict={}
        
        for i in dict.keys():
            if dict[i] not in reversedDict:
                reversedDict[dict[i]] = [i]
            else:
                reversedDict[dict[i]].append(i)
                
        li = sorted(reversedDict.keys(), reverse = True)
        
        ans =[]
        
        counter=0
        while counter < len(li):
            innerCounter=0
            while len(ans) <k and innerCounter < len(reversedDict[li[counter]]):
                ans.append(reversedDict[li[counter]][innerCounter])
                innerCounter+=1
            
            counter+=1
                
              
                
                
        return ans