class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        res=str(n)
        c=str(x)
        if (res[0]!=c) and c in res:
            return True
        return False
        