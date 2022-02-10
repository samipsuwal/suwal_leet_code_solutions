# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        li=[]
        
        def bfs(node):
            if node:
                li.append(node.val)
                bfs(node.left)
                bfs(node.right)
                
        bfs(root)
        
        return len(set(li))==1
        
        
        