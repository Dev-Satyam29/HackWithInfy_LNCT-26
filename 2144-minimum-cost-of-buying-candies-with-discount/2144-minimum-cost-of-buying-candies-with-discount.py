class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        c=0
        summ=0
        for i in cost:
            if c!=2:
                summ+=i
                c+=1
            else:
                c=0
                pass
        return summ
        