class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countOnes(n):
            count =0
            if n!=0:
                while n>=1:
                    if n%2 ==0:
                        n= n//2
                    else:
                        n = (n-1)//2
                        count+=1
                        
            return count
        
        li=[]
        for i in range(n+1):
            li.append(countOnes(i))
            
        return li