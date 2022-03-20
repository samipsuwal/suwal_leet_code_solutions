class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        arr ={1,2,3,4,5}
        curr={3,4,5}
        
        
        while len(arr)<=5000:
            temp =set()
            for i in curr:
                temp.add(i*2)
                temp.add(i*3)
                temp.add(i*5)
                
            arr.update(temp)
            curr=temp
            
            
        li = sorted(list(arr))
        return li[n-1]
            
        