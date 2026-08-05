# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 

        while curr: 
            nxt = curr.next #we remeber that B will be next to connect
            #Now before we change curr we just tell prev
            curr.next = prev
            prev = curr 
            curr = nxt
        return prev
