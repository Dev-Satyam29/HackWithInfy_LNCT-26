class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxi=max(nums)
        arr=[]
        for i in range(1,maxi+1):
            arr.append(i)
        arr.append(maxi)
        if sorted(nums)==sorted(arr):
            return True
        else:
            return False
       
        
        