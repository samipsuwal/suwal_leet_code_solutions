# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        aDict={}
        
        def isPali(li):
            if len(li) ==1:## edge case
                return True
            if len(li)%2!=0:
                return False
            for i in range(len(li)//2):
                if li[i]!=li[len(li)-1-i]:
                    return False
                
            return True
        
        
        def bfs(node, depth):
            if not node:
                if depth not in aDict.keys():
                    aDict[depth] = [-101]
                else:
                    aDict[depth].append(-101)
                return 
            
            if depth not in aDict.keys():
                aDict[depth] = [node.val]
            else:
                aDict[depth].append(node.val)
            
            depth += 1
            bfs(node.left, depth)
            bfs(node.right, depth)
            
            
        bfs(root, 0)   
        
        print(aDict)
        
        for li in aDict.keys():
            if not isPali(aDict[li]):
                return False
            
            
        return True
        
            
            
            
        
        
        
        
            
            
            
    
            
        