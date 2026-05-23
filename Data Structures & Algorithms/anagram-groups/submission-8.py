class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getValue(s: str) -> List:
            val = [0] * 26
            for c in s:
                val[ord(c) - ord('a')] += 1
            return tuple(val)
        
        wordVals = {}
        for word in strs:
            val = getValue(word)

            if val not in wordVals:
                wordVals[val] = []

            wordVals[val].append(word)

        output = []
        
        for val in wordVals.values():
            output.append(val)

        return output