# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        hashmap = {0:0}
        
        
        def treeTraversal(node):
            if not node:
                return
            
            
            if node.val >= low and node.val <= high:
                hashmap[0] = hashmap[0] + node.val
                
            treeTraversal(node.left)
            treeTraversal(node.right)
            
        
        treeTraversal(root)
        
        return hashmap[0]
        