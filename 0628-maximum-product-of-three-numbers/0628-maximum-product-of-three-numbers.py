class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res=1
        n=len(nums)
        ans_pos=nums[0]*nums[1]*nums[-1]
        ans_neg=nums[-1]*nums[-2]*nums[-3]
        res=max(ans_pos,ans_neg)
        return res
        
        