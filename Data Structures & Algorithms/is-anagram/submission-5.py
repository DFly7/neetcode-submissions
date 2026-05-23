class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
            hashmap[t[i]] = -1 + hashmap.get(t[i], 0)

        flag = all(value == 0 for value in hashmap.values())

        return flag        

        

        