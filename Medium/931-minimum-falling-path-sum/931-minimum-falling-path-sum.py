class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = m = len(matrix)
        arr = []


        for i in range(m):
            li =[]
            for j in range (n):

                if i ==0:
                    li.append(matrix[i][j])
                else:
                    if j-1<0:
                        candi = min(arr[i-1][j],arr[i-1][j+1])
                    elif j+1>m-1:
                        candi = min(arr[i-1][j-1],arr[i-1][j])
                    else:
                        candi = min(arr[i-1][j-1], arr[i-1][j],arr[i-1][j+1])
                    li.append(matrix[i][j]+candi)
            arr.append(li)

        arr[-1].sort()
        return arr[-1][0]