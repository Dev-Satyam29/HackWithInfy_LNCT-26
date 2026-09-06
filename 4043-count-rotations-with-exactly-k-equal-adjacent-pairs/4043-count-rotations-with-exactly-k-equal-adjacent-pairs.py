class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        count=0
        for i in range(n):
            if s[i]==s[(i+1)%n]:
                count+=1
        diff=n-count
        if k==count:
            return diff
        if k==count-1:
            return count
        return 0
        