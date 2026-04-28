class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        max_i=max(nums)
        min_i=min(nums)
        for i in range(min_i,max_i+1):
            if i not in nums:
                res.append(i)
        return res
        