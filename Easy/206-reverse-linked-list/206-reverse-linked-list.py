# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        arr=[]
        ans=[]
        while head:
            arr.append(head)
            head = head.next
            
        for i in range(len(arr)-1, -1, -1):
            print(i)
            if i ==0:
                arr[i].next= None
            else:
                arr[i].next = arr[i-1]
            ans.append(arr[i])
            
        return ans[0]
        
            