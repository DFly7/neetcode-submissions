class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        letters = [0] * 26

        for i in range(len(s)):

            letter1 = s[i]
            letter2 = t[i]

            num1 = ord(letter1) - ord('a')
            num2 = ord(letter2) - ord('a')

            letters[num1] += 1
            letters[num2] -= 1

        for n in letters:
            if n != 0:
                return False
        return True
