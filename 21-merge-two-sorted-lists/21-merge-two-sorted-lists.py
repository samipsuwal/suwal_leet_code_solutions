# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        arr =[]
        
        while list1:
            
            arr.append(list1.val)
            list1 = list1.next
            
        while list2:
            arr.append(list2.val)
            list2 = list2.next
          
        if len(arr)==0:
            return None
        
        arr.sort()
        
        ans =[]
        for i in range(len(arr)):
            curr = ListNode()
            curr.val = arr[i]
            ans.append(curr)
            
        print(ans)
        for i in range(len(ans)-1):
            ans[i].next = ans[i+1]
            
        return ans[0]
        