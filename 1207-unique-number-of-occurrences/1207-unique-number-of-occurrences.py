class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        res=[]
        for k,v in freq.items():
            if freq[k] in res:
                return False
            else:
                res.append(freq[k])
        return True
        