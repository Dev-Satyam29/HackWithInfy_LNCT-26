class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        s=str(num)
        for i in range(len(s)-(k-1)):
            temp=int(s[i:i+k])
            if temp!=0:
                if num%temp==0:
                    count+=1
        return count
        