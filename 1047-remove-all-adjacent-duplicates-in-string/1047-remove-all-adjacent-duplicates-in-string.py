class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        a=''
        for i in stack:
            a+=i
        return a
        