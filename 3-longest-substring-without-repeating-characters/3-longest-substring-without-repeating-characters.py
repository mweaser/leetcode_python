class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        maxLength = 0
        freq = {}
        
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            
            if rightChar in freq:
                windowStart = max(windowStart, freq[rightChar] + 1)
            freq[rightChar] = windowEnd
            
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        return maxLength