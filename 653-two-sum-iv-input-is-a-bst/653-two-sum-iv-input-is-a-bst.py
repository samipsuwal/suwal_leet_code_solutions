# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dict=[]
        ans=[]
        def bfs(node):
            #print(dict)
            if node:
                if (k-node.val) not in dict:
                    dict.append(node.val)
                    bfs(node.left) 
                    bfs(node.right)
                else:
                    ans.append(node.val)

            
        
        bfs(root)
        if len(ans) > 0:
            return True
        else:
            return False
        