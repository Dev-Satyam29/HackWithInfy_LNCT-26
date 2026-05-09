class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max_freq=-1
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if freq[k]==k:
                max_freq=max(k,max_freq)
                
        return max_freq
        