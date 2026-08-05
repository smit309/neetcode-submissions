class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            while s[right] in output:
                output.remove(s[left])
                left += 1

            output.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength        

