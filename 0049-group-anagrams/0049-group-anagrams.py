class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        for words in strs:
            sorted_words=''.join(sorted(words))
            anagram_map[sorted_words].append(words)
        return list(anagram_map.values())
        