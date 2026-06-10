class Solution:
    """ 
        so approach is that if we slide. variable sized window 
        we need to know if we have saw this char in the window before
        so we need to use a set, and as a char enters window check if its in
        set, as it leaves remove from set. 
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        saw = set()
        max_length = 0

        for r in range(len(s)):
            
            while s[r] in saw:
                saw.remove(s[l])
                l += 1
            
            saw.add(s[r])

            max_length = max(max_length, r - l + 1)
        return max_length