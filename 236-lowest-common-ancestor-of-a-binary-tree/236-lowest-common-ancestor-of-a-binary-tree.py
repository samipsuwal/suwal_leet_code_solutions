# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pParent=[]
        qParent=[]
        def dfs(root, target, li):
            if root is None:
                return False
            
            li.append(root)
            if root.val == target:
                return True
            right = dfs(root.right, target, li)
            left = dfs(root.left, target, li)
            if right == False and left == False:
                li.pop()
            
            return right or left
            
        dfs(root, p.val,pParent)
        dfs(root, q.val,qParent)
        
        smaller=[]
        larger=[]
        if len(qParent)<len(pParent):
            smaller = qParent
            larger = pParent
        else:
            larger = qParent
            smaller = pParent
            
        for i in range(len(smaller)-1,-1,-1):
            for j in larger:
                if smaller[i] == j:
                    return j
            
            
            
            
            
            
            