class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in hashmap.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif stack.pop() != hashmap[c]:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

        