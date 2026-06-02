class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        p=str(n)
        freq={}
        for i in p:
            freq[i]=freq.get(i,0)+1
        summ=0
        for k,v in freq.items():
            summ+=int(k)*int(freq[k])
        return summ
        