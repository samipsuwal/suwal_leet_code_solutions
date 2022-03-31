# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder ) <=0:
            return
        
        
        root = TreeNode()
        root.val = preorder[0]
        preorder.pop(0)
        
        def bfs(curr, root):
            
            #place item in binary tree
            if curr <= root.val:
                if root.left is None:
                    root.left = TreeNode(curr)
                else:
                    bfs(curr, root.left)
            else: 
                if root.right is None:
                    root.right = TreeNode(curr)
                else:
                    bfs(curr, root.right)
            
            
        for i in preorder:
            bfs(i, root)
            
        return root
            
        
        