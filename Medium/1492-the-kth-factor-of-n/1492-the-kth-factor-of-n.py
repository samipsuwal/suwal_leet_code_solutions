class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        fact = {}
        counter = 1
        for i in range(1,n+1):
            if n%i ==0:
                fact[counter] = i
                counter+=1

        if k in fact.keys():
            return fact[k]

        return -1
        
        