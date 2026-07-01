class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr=list(address)
        s=''
        for i in range(len(arr)):
            if arr[i]=='.':
                arr[i]='[.]'
                s+=arr[i]
            else:
                s+=arr[i]
        return s
        