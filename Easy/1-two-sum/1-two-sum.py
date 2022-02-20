class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #redoing this for O(n)
        #traverse through this setup a hashmap

        #lot better implementation after watching the soluion, regarding duplicate keys
        
        aDict = {}
        
        for i in range(len(nums)):
            aDict[nums[i]] = i
            
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in aDict and aDict[compliment] != i:
                return [i, aDict[compliment]]
            
            
            #leethub test
            #changed2
                      
        