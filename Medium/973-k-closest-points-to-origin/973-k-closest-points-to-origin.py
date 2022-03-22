class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
       
        dict={}
        
        for point in points:
            key = point[0]**2 + point[1]**2
            if key not in dict:
                dict[key] = [point]
            else:
                dict[key].append(point)
                
        print(dict)
                
        li = list(dict.keys())
        
        li.sort()
        
        ans = []
        
        counter =0
        while len(ans) < k:
            for i in dict[li[counter]]:
                ans.append(i)
            counter+=1
            
        return ans