class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        p=money
        prices.sort()
        if prices[0]>=money:
            return money
        money-=prices[0]
        if money<prices[1]:
            return p
        else:
            return money-prices[1]
        