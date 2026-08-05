class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {} 

        for count in s:
            freq[count] = freq.get(count,0) + 1

        for count in t:
            if count not in s:
                return False
            freq[count] -= 1
        
            if freq[count] < 0:
                return False
        return True                     