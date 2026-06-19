class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum=0
        squareSum=0
        while n>0:
            num=n%10
            digitSum+=num
            squareSum+=num**2
            n=n//10
        if squareSum-digitSum>=50:
            return True
        else:
            return False
        