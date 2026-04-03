class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ele=max(nums)
        for i in range(len(nums)):
            if nums[i]==max_ele:
                pass
            elif nums[i]!=max_ele and (2*nums[i])<=max_ele:
                pass
            else:
                return -1
        return nums.index(max_ele)
        