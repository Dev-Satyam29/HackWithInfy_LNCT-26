class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summ=0
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if freq[k]==1:
                summ+=k
        return summ
        