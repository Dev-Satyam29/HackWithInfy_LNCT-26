class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dis=float('-inf')
        summ=0
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    summ=abs(j-i)
                    max_dis=max(summ,max_dis)
        return max_dis
        