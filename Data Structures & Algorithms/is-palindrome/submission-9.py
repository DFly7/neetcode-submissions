class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()
        
        #searched for this line to remove none letter chars
        # s = ''.join(char for char in s if char.isalpha())

        if len(s) == 0:
            return True
        
        for i in range(len(s)):
            if not (s[start].isalpha() or s[start].isdigit()):
                start += 1
                continue
            elif not (s[end].isalpha() or s[end].isdigit()):
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            elif start > end:
                return True
            start += 1
            end -= 1
        return True