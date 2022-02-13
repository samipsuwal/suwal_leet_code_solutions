# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        sumOfLeftNodes ={0:0}
        
        def bfs(node, isLeft):
            if not node:
                return sumOfLeftNodes
            
            if isLeft and not node.left and not node.right:
                sumOfLeftNodes[0] = sumOfLeftNodes[0] +node.val
                print(sumOfLeftNodes)
                #return sumOfLeftNodes
            else:
                bfs(node.left, True)
                bfs(node.right, False)

            
        bfs(root, False)      
                    
        return sumOfLeftNodes[0]
        
        