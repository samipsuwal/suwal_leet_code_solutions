# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        
        
        #traverse and record depth and the parent
        ans = {} #key is depth and parent is value
        
        def bfs (node, parent, depth):
            if not node:
                return
            
            if node.val == x or node.val == y:
                ans[parent] = depth
                
            depth += 1
            bfs(node.left, node.val, depth)
            bfs(node.right, node.val, depth)
            
        if root.val == x or root.val == y:
            return False
        
        bfs(root, None, 0)
        
        li =[]
        ##reduce(set.union, ans.values())
        for i in ans.keys():
            li.append(ans[i])
        
        if len(set(li))==1 and len(set(ans.keys()))==2:
            return True
        
        return False
                
            
        