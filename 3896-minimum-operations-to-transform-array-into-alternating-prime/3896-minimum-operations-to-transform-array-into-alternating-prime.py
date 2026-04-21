class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def isprime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        n=len(nums)
        c=0
        for i in range(n):
            if i%2==0:
                if isprime(nums[i])==True:
                    pass
                else:
                    while not isprime(nums[i]):
                        c+=1
                        nums[i]+=1
            if i%2==1:
                if isprime(nums[i])==False:
                    pass
                else:
                    while isprime(nums[i]):
                        c+=1
                        nums[i]+=1
        return c


        