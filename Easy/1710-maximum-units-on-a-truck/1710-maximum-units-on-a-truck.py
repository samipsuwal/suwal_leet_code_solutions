class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        units = []
        
        for boxType in boxTypes:
            for i in range(boxType[0]):
                units.append(boxType[1])
                
        units.sort()
        #print(units)
        ans=0
        for i in range(truckSize):
            if units:
                ans+= units.pop()
            else:
                break
            
        
        return ans
        
        