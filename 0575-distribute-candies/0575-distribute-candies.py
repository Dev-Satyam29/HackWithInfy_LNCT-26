class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        doc=n/2
        arr=list(set(candyType))
        count=0
        for i in arr:
            if count<doc:
                count+=1
            else:
                break
        return count
        