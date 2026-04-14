class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        res=[]
        for ch in order:
            if ch in freq:
                res.append(ch*freq[ch])
                del freq[ch]
        for ch in freq:
            res.append(ch*freq[ch])
        return "".join(res)