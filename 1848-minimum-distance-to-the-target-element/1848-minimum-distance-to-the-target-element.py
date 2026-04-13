class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n=len(nums)
        min_ans=float('inf')
        for i in range(n):
            if nums[i]==target:
                ans=abs(i-start)
                min_ans=min(min_ans,ans)
        return min_ans
        