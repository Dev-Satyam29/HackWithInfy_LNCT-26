class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank = {}
        for i, val in enumerate(sorted_unique):
            rank[val] = i + 1
        return [rank[x] for x in arr]