class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        lar=1
        for i in range(1,mini+1):
            if mini%i==0 and maxi%i==0:
                lar=max(lar,i)
        return lar
      
        