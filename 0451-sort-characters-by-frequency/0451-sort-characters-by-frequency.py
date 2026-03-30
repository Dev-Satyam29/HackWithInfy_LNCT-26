class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        sorted_d = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        s1=''
        for key,val in sorted_d.items():
            s1+=key*val
        return s1

        