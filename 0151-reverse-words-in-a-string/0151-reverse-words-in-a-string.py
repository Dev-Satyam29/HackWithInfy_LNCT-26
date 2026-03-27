class Solution:
    def reverseWords(self, s: str) -> str:
        sen=s.split()
        n=len(sen)
        left=0
        right=n-1
        while left<right:
            sen[left],sen[right]=sen[right],sen[left]
            left+=1
            right-=1
        res=' '.join(sen)
        return res

        