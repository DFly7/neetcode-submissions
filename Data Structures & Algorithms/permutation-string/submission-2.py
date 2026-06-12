class Solution:
    """
        so idea that helped me on thsi one was 
        that we just need to know if s1 is in s2

        so we slide a window over s2 of size s1, and for every sub string size s1 we 
        check to see if the char count match, ie the id.
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            s1_count[index] += 1
        print(s1_count)
        
        char_count = [0] * 26

        # Pre seed it with the first window not including the last as we add it after
        for i in range(len(s1) - 1):
            index = ord(s2[i]) - ord('a')
            char_count[index] += 1
        print(char_count)
        l = 0

        for r in range(len(s1) - 1, len(s2)):
            print(f'r = {r}, l = {l}, array = {s2[l:r+1]}')

            r_index = ord(s2[r]) - ord('a')
            char_count[r_index] += 1
            print(s1_count)
            print(char_count)
            if char_count == s1_count:
                return True
            
            l_index = ord(s2[l]) - ord('a')
            char_count[l_index] -= 1
            l += 1

            
        return False
            

