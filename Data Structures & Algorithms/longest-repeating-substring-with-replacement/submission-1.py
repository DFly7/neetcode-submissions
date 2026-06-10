from collections import defaultdict
class Solution:
    """
        Yeah so thsi one we will slide a variable sized window over s
        we will keep track of what the most fequent char in teh window is as 
        we knwo that window is valid if

        len window - max frequ char <= target replacement

        as we only need to replace len window - max frequ char for the the window to be valid

        if window is not valid we just move l += 1 until it is valid 
    """
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        max_freq = 0
        max_length = 0

        for r in range(len(s)):
            count[s[r]] += 1 

            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
 

        return max_length
        