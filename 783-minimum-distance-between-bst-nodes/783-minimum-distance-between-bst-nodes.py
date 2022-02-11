# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        li=[]
        def bfs(node):
            if node:
                li.append(node.val)
                
                bfs(node.left)
                bfs(node.right)
        
        
        bfs(root)
        mini=sys.maxsize
        li.sort()
        for i in range(len(li)-1):
            mini = min(mini, li[i+1] - li[i])
            
            
        return mini
            
        