# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        
        li=[] #since size is 2 guaranteed
        
        def bfs(node):
            if node:
                li.append(node.val)
                
                bfs(node.left)
                bfs(node.right)
                
        bfs(root)
        
        li.sort()
        
        if len(li) == 2:
            return li[1]- li[0]
        
        mini = sys.maxsize
        for i in range(len(li)-1):
            mini = min(li[i+1] - li[i],mini)
        
        return mini
                    
                