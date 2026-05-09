class Solution:
    def isprime(self,num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    def sumOfPrimesInRange(self, n: int) -> int:
        summ=0
        di=str(n)
        re=di[::-1]
        final=int(re)
        range1=min(n,final)
        range2=max(n,final)
        for i in range(range1,range2+1):
            if self.isprime(i)==True:
                summ+=i
        return summ
        