class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for i in nums:
            p=i**2
            res.append(p)
        return sorted(res)
        