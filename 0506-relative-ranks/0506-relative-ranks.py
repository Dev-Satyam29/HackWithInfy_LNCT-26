class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        freq={}
        s=sorted(score,reverse=True)
        if len(s)>0:
            freq[s[0]]="Gold Medal"
        if len(s)>1:
            freq[s[1]]="Silver Medal"
        if len(s)>2:
            freq[s[2]]='Bronze Medal'
        for i in range(3,len(s)):
            freq[s[i]]=str(i+1)
        res=[]
        for i in score:
            res.append(freq[i])
        return res
        