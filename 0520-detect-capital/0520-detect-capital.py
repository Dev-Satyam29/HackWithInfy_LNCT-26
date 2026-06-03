class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper() or word==word.lower() :
            return True
        elif word[0]==word[0].upper() and word[1:len(word)]==word[1:len(word)].lower():
            return True
        else:
            return False


        