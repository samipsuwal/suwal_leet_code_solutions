"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return None
        
        def deconstructBinaryTree(root, arr):
            if root is None:
                return arr
            
            left = deconstructBinaryTree(root.left, arr)
            right = deconstructBinaryTree(root.right, arr)
            
            return left + [root] + right
        
        arr = deconstructBinaryTree(root, [])
        
        prev = arr[-1]        
        for index in range(len(arr)):
            arr[index].left = prev
            if index+1 >= len(arr):
                index=-1
            arr[index].right = arr[index+1]
            prev = arr[index]
            
            
        return arr[0]
            
            
            
            
            