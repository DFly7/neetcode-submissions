class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}

        for l in s:
            if l in sMap:
                sMap[l] += 1
            else:
                sMap[l] = 1
        tMap = {}
        for l in t:
            if l in tMap:
                tMap[l] += 1
            else:
                tMap[l] = 1
 
        return sMap == tMap