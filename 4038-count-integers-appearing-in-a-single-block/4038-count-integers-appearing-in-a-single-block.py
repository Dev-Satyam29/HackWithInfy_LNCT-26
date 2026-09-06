class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        freq={}
        freq[nums[0]]=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                freq[nums[i]]=freq.get(nums[i],0)+1
        count=0
        for v in freq.values():
            if v==1:
                count+=1
        return count
        
        