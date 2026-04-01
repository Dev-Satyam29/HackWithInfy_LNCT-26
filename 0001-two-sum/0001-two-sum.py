class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_={}
        for x,y in enumerate(nums):
            complement=target-y
            if complement in hash_:
                return[hash_[complement],x]
            hash_[y]=x
        