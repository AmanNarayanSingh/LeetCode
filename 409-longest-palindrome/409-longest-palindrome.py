class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                seen.remove(char)
        
        return len(s) - max(0, len(seen) - 1)