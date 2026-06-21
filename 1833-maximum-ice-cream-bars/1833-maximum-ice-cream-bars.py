class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s=0
        for i in range(len(costs)):
            if costs[i]<=coins and coins!=0:
                s+=1
                coins-=costs[i]
            else:
                break
        return s