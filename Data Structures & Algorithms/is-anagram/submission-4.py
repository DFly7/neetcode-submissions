class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
            if t[i] in hashmap:
                hashmap[t[i]] -= 1
            else:
                hashmap[t[i]] = -1

        flag = all(value == 0 for value in hashmap.values())

        return flag        

        

        