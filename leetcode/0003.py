class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        current = {s[0]}
        i = 0
        j = 1
        biggest = 0
  
        while j < len(s):
            # move i forward until s[j] is no longer counted
            if s[j] in current:
                while s[j] in current:
                    current.remove(s[i])
                    i += 1
            current.add(s[j])
            biggest = max(biggest, len(current))

            j += 1
        return biggest
