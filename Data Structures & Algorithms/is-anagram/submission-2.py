class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = {}
        tHashMap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sHashMap[s[i]] = 1 + sHashMap.get(s[i], 0)
            tHashMap[t[i]] = 1 + tHashMap.get(t[i], 0)

        for c in sHashMap:
            if sHashMap[c] != tHashMap.get(c, 0):
                return False

        return True

        