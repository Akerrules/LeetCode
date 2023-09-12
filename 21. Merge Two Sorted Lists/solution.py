# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #iterate through both list and first 
        #current is the lower value between two point and next is the higher
        
        if(list1==None):
            return list2
        elif(list2==None): 
            return list1
        
        result = list1
        head_1 = list1
        head_2 = list2
        if(list1.val>list2.val):
            head_1 = list2
            head_2 = list1
            result = list2
        # print(head_1.val, head_2.val)
        while(head_1 !=None and head_2 !=None):
            if(head_1.next==None and head_2!=None): ## add end
                # print("1", head_2.val)
                head_1.next = head_2
                head_2=None
            elif(head_2.val>=head_1.val and head_2.val <= head_1.next.val): # between
                temp = ListNode(head_2.val,head_1.next)
                head_1.next=temp
                # print("2",temp.val)
                head_2 = head_2.next
            elif(head_2.val<=head_1.val): ## first
                # print("3", head_2.val, head_1.val)  
                temp = ListNode(head_2.val,head_1)
                head_1 = temp
                head_2 = head_2.next 
                   
            head_1 = head_1.next

        return result