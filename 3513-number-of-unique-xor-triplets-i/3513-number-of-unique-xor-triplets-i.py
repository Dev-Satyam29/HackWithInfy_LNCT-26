class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        mask=0
        for i in nums:
            mask |=i
        return mask+1

        