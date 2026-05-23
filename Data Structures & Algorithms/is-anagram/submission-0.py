class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = {}
        tHashMap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in sHashMap:
                sHashMap[s[i]] += 1
            else:
                sHashMap[s[i]] = 1
            if t[i] in tHashMap:
                tHashMap[t[i]] += 1
            else:
                tHashMap[t[i]] = 1

        return (sHashMap == tHashMap)

        