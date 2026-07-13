class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr = []
        low_len = len(str(low))
        high_len = len(str(high))
        for length in range(low_len, high_len + 1):
            num = 0
            for i in range(1, length + 1):
                num = num * 10 + i
            arr.append(num)
            current = num
            last_digit = length
            while last_digit < 9:
                current = (current % (10 ** (length - 1))) * 10 + (last_digit + 1)
                last_digit += 1
                arr.append(current)
        ans = []
        for num in arr:
            if low <= num <= high:
                ans.append(num)

        return ans