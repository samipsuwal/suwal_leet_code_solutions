class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        j = len(numbers)-1
        i=0
        
        for k in range(len(numbers)):
            if (numbers[i] + numbers[j])>target:
                j-=1
            elif (numbers[i] + numbers[j])<target:
                i+=1
            else:
                return [i+1,j+1]
        
        
        