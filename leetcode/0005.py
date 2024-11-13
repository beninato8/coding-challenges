class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggest = 0
        pal = ''
        for i in range(len(s)):
            remainder = len(s) - i
            if remainder * 2 <= biggest:
                break
            for j in range(0, remainder):
                if s[i - j] != s[i + j]:
                    break
                if i + j >= len(s) or j > i:
                    break

                if 1 + 2 * j > biggest:
                    biggest = 1 + 2 * j
                    pal = s[i-j:i+j+1]
            
            for j in range(0, remainder - 1):
                if s[i - j] != s[i + j + 1]:
                    break
                if i + j + 1 >= len(s) or j > i:
                    break

                if 2 + (2 * j) > biggest:
                    biggest = 2 + 2 * j
                    pal = s[i-j:i+j+2]

        return pal

