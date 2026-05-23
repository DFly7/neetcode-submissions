class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {} 

        if len(s) != len(t):
            return False

        for c in s:
            word1[c] = word1.get(c, 0) + 1

        for l in t:
            word2[l] = word2.get(l, 0) + 1

        return word1 == word2


        