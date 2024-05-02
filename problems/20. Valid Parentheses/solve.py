class Solution:
    validation_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif c in self.validation_dict.keys():
                try:
                    last = stack.pop()
                    if self.validation_dict[c] != last:
                        return False
                except:
                    return False
        if len(stack) != 0:
            return False
        return True

solution = Solution()
print(solution.isValid("((([[]])))"))



