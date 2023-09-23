# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        cur= ListNode()
        result= cur
        carry = 0
       
        while l1!=None or l2!=None:
            v1,v2 = 0,0
            if(l1!=None):
                v1= l1.val
                l1 = l1.next
            if(l2!=None):
                v2 = l2.val
                l2 = l2.next
            value =  v1 + v2 +carry
            cur.next = ListNode(value%10,None)
            carry = int(value/10)
            cur = cur.next
        if(carry!=0):
            cur.next = ListNode(carry)
           
        return result.next