class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        arr =[]
    
        counter =0
        while counter < numRows:
            li =[]
            for i in range(counter+1):
                if i ==0 or i==counter:
                    li.append(1)
                else:
                    li.append(arr[counter-1][i-1]+arr[counter-1][i])
            arr.append(li)
            counter+=1

        return arr
