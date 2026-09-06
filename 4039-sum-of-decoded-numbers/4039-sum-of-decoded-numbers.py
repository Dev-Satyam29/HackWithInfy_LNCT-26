class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        n=len(nums)
        mod=(10**9)+7
        width=0
        d=0
        x=0
        y=0
        total=0
        for i in nums:
            width=i%10
            d=i//10
            d=str(d)
            x=int(d[:width])
            y=int(d[width:])
            total=(total+pow(x,y,mod))%mod
        return total

        