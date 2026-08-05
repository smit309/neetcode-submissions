class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check edge cases 
        if len(s) != len(t):
            return False 


        #iterate through whole s string and store their freq into count
        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1

        #iterate though string t and do count - if exist and if not then return false 
        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0: 
                return False

        return True                    