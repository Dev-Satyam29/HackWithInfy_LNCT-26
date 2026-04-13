class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        rev=sorted(heights)
        count=0
        for a,b in  zip(heights,rev):
            if a!=b:
                count+=1
        return count
        