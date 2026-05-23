class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += s
            output += "'"
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        word = ""
        for c in s:
            if c != "'":
                word += c
            else:
                output.append(word)
                word = ""
        return output

