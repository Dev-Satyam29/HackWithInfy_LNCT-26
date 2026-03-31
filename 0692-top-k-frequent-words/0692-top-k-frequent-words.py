class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}
        for i in words:
            freq[i]=freq.get(i,0)+1
        sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
        return sorted_words[:k]
        
            
        