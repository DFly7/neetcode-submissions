class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sChar = s[i]
            tChar =t[i]

            sMap[sChar] = sMap.get(sChar, 0) + 1
            tMap[tChar] = tMap.get(tChar, 0) + 1

        return sMap == tMap
