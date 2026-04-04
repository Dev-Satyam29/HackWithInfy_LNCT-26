# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def binary_to_decimal(n):
            res = 0
            base = 1
            
            while n:
                res += (n % 10) * base
                base *= 2
                n //= 10
            
            return res
        curr=head
        n=0
        while curr is not None:
            n=(n*10)+curr.val
            curr=curr.next
        return binary_to_decimal(n)

        