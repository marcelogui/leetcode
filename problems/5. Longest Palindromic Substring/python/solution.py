class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = len(s)
        longest = ""
        while end != 0:
            if len(longest) >= end:
                return longest
            test = s[start:end]
            if self.isPalindrome(test) and len(test) > len(longest):
                longest = test
            start += 1
            if start >= end:
                start = 0
                end -= 1
        return longest

    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True

a = Solution()
print(a.longestPalindrome("abracacarba"))

