# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res=[]
        curr=head
        while curr is not None:
            res.append(curr.val)
            curr=curr.next
        left,right=0,len(res)-1
        while left<=right:
            if res[left]==res[right]:
                pass
            else:
                return False
            left+=1
            right-=1
        return True
        