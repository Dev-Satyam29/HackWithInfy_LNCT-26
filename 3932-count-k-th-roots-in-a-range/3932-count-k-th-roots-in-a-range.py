class Solution:
        def countKthRoots(self, l: int, r: int, k: int) -> int:
            if k == 1:
                return r - l + 1
            return sum(l <= x ** k <= r for x in range(int(r ** (1 / k)) + 2))
            