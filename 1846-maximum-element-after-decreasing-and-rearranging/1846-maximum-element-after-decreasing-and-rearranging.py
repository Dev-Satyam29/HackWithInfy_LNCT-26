class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        ar=[]
        arr.sort()
        arr[0]=1
        ar.append(arr[0])
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])<=1:
                ar.append(arr[i])
            else:
                new=arr[i-1]+1
                arr[i]=new
                ar.append(new)
        return max(ar)

        