class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def isHashMapValid(hm):
            if len(hm.keys()) >2:
                return False
            return True
        
        def countOfValuesInHashMap(hm):
            count =0
            for i in hm.keys():
                count+= hm[i]
            return count
        
        hm={}#store fruit type and number
        
        i=0
        maxCount = 0
        for f in fruits:
            if f not in hm:
               hm[f] = 1
            else:
                hm[f] +=1
                
            while not isHashMapValid(hm):
                if hm[fruits[i]] ==1:
                    hm.pop(fruits[i])
                else:
                    hm[fruits[i]] -=1
                    
                i+=1
            maxCount = max(maxCount, countOfValuesInHashMap(hm))
        
        return maxCount
                
                
        
        