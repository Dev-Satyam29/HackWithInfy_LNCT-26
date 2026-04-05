# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        curr=head
        while curr is not None:
            count+=1
            curr=curr.next
        if n==count:
            return head.next
        prev=head
        for _ in range(count-n-1):
            prev=prev.next
        prev.next=prev.next.next
        return head
        