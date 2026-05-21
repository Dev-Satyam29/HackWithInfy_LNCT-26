class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d=s1.split(' ')
        f=s2.split(' ')
        arr=[]
        freq1={}
        freq2={}
        for ch in d:
            freq1[ch]=freq1.get(ch,0)+1
        for ch in f:
            freq2[ch]=freq2.get(ch,0)+1
        for i in d:
            if i not in f and freq1[i]==1:
                arr.append(i)
        for j in f:
            if j not in d and freq2[j]==1:
                arr.append(j)
        return arr
        