class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        dup=0
        miss=0
        for k,v in freq.items():
            if freq[k]==2:
                dup=k
        for i in range(1,len(nums)+1):
            if i not in freq:
                miss=i
        return [dup,miss]

        