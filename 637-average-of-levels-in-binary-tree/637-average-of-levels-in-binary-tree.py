# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        nodesCount={}
        valCount={}

        def bfs(node, level):
            if node:
                if level in nodesCount.keys():
                    nodesCount[level] += 1
                else:
                    nodesCount[level] =1
                    
                if level in  valCount.keys():
                    valCount[level] += node.val
                else:
                    valCount[level] = node.val
                    
                bfs(node.left, level+1)
                bfs(node.right, level+1)
                
            
        bfs(root,0)


        print(nodesCount)
        print(valCount)
        
        ans =[]
        for i in nodesCount.keys():
            ans += [valCount[i]/nodesCount[i]]
            
            
        return ans
        
        
        
        
        
        