class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []

        for s in strs:
            array = [0] * 26

            for c in s:
                arrayNum = ord(c) - ord('a')
                array[arrayNum] += 1

            if tuple(array) in hashMap:
                hashMap[tuple(array)].append(s)
            else:
                hashMap[tuple(array)] = [s]
        
        return hashMap.values()
