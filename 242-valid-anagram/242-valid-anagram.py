class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        l1 = []
        l2=[]
        for i in s:
            l1.append(i)
            
        for i in t:
            l2.append(i)
            
        l1.sort()
        l2.sort()
        
        return l1==l2
        