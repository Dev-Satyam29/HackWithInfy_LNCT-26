class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        arr=[]
        count=0
        for i,v in freq.items():
            if freq[i]==1:
                count+=1
                if count==k:
                    return i
        return ""
        
        