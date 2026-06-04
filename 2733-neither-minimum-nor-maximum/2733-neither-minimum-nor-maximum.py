class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        for i in nums:
            if i!=maxi and i!=mini:
                return i
        return -1
        