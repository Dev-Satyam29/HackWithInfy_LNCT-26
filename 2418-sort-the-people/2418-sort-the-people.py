class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired=list(zip(heights,names))
        paired.sort(reverse=True)
        res=[]
        for h,n in paired:
            res.append(n)
        return res
        