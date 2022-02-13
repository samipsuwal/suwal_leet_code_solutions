# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        
        ans = []
        
        
        def bfs(node):
            if not node:
                return
            
            if node.left and not node.right:
                #print("left lonely")
                ans.append(node.left.val)
                bfs(node.left)
            elif node.right and not node.left:
                #print("right lonley")
                ans.append(node.right.val)
                bfs(node.right)
            else:
                #print("both present")
                bfs(node.left)
                bfs(node.right)
                
                
        bfs(root)
        return ans
            
        