# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curHead = head
        node   = None
        prevnode =None
        while curHead!=None:
            
            node = curHead
            curHead = curHead.next
            node.next = prevnode
            prevnode = node     
        return prevnode