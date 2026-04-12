class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res=[]
        for i in nums:
            for d in str(i):
                res.append(int(d))
        freq={}
        for i in res:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if k==digit:
                return freq[k]
        return 0
        