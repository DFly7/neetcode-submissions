class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxSub = 0 
        saw = {}

        for r in range(len(s)):

            if s[r] in saw and saw[s[r]] >= l:
                l = saw[s[r]] + 1 

            lengSub = r - l + 1
            maxSub = max(lengSub, maxSub)
            saw[s[r]] = r
        return maxSub


            
