class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dblArr=grid
        perimeter =0
        for i in range(len(dblArr)):
            for j in range(len(dblArr[0])):
                if dblArr[i][j]:
                    #check if water in the left
                    if (i-1)< 0 or dblArr[i-1][j] ==0:
                        perimeter +=1
                    #check if water on the top
                    if (j-1) < 0 or dblArr[i][j-1] ==0: 
                        perimeter +=1
                    #check if water in the right
                    if (i+1) >= len(dblArr) or dblArr[i+1][j] ==0:
                        perimeter +=1
                    #check if water on the bottom
                    if (j+1) >= len(dblArr[0]) or dblArr[i][j+1] ==0: 
                        perimeter +=1
        return perimeter
