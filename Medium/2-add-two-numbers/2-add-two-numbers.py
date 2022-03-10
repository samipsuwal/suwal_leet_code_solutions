# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def createNodeListFromString(s, index):

            if index <0:
                return None

            lN = ListNode()
            lN.val = s[index]
            lN.next = createNodeListFromString(s, index-1)


            return lN
        
        
        counter =0
        
        n1 = 0
        n2=0
        
        while l1:
            n1+= l1.val * 10 ** counter
            counter+=1
            l1 = l1.next
            
        counter =0
        while l2:
            n2+= l2.val * 10 ** counter
            counter+=1
            l2 = l2.next
            
        n3 = n1+n2
        
        
        stringRep = str(n3)
        
        ans = createNodeListFromString(stringRep, len(stringRep)-1)
        
        return ans
            
            
        
        
        