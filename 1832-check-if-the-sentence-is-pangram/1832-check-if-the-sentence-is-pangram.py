class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sam='abcdefghijklmnopqrstuvwxyz'
        for i in sam:
            if i not in sentence:
                return False
        return True

        