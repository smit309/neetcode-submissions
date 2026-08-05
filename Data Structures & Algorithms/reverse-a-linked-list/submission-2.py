# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # None -> 1 -> 2 -> 3 
        while curr:
            # nxt = 2 remebering
            nxt = curr.next 
            # we have to tell okay now 1 points to prev
            curr.next = prev
            prev = curr 
            curr = nxt

        return prev

