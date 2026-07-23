'''class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        mask=0
        for i in nums:
            mask |=i
        return mask+1'''
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
            n = len(nums)
            m = n
            
            m |= m >> 1
            m |= m >> 2
            m |= m >> 4
            m |= m >> 8
            m |= m >> 16
            
            return (m + 1) >> (3 // (n + 1))

            