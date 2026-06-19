class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        low=max(1,n-k)
        high=n+k
        s=0
        for i in range(low,high+1):
            if (n&i)==0:
                s+=i
        return s
        