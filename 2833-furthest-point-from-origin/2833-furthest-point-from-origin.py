class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count=moves.count('_')
        countl=moves.count('L')
        countr=moves.count('R')
        return abs(countl-countr)+count