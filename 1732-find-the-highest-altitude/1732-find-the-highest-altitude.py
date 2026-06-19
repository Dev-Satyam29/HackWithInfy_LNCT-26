class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr=[]
        arr.append(0)
        for i in range(len(gain)):
            s=arr[i]+gain[i]
            arr.append(s)
        return max(arr)
        