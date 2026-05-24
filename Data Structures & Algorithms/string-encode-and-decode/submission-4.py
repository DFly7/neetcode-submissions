class Solution:
    # Delim # -> #4 delim then 4 letter word
    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += f'{len(word)}#{word}'
        return out

    def decode(self, s: str) -> List[str]:
        encoded = list(s)
        out = []
        i = 0
        while i < len(encoded):
            # 1. Find where the '#' is. 
            # Everything from the current 'i' up to this '#' is the number.
            j = i
            while s[j] != '#':
                j += 1

            # 2. Extract the length and convert to integer
            length = int(s[i:j])

            # 3. The word starts right after '#' (j + 1) 
            # and ends exactly 'length' characters later
            word = s[j + 1 : j + 1 + length]
            out.append(word)
            
            # 4. Move your pointer to the start of the next encoded block
            i = j + 1 + length
        return out
            




