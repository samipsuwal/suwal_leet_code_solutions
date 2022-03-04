class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr  = []
    
        if n%2 ==0:#starts from 2
            counter =1
            for i in range(n):
                arr.append(counter)
                if counter > 0:
                    counter *= -1
                else:
                    counter *= -1
                    counter +=1
        else:
            arr.append(0)
            counter =1
            for i in range(1,n):
                arr.append(counter)
                if counter > 0:
                    counter *= -1
                else:
                    counter *= -1
                    counter +=1
        return arr