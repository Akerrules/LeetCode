# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
				#dic = {}
        # while head!=None:
        #     if(id(head) in dic):
        #       return True
        #     dic[id(head)] = id(head)
        #     head = head.next

        # return False

        if(head==None):
            return False
        head1 = head
        head2 = head.next

        while head1!=head2:
            if(head2==None or head2.next==None):
                return False
            head1 = head1.next
            head2 = head2.next.next
            
            
        return True