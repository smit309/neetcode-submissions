class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we have two strings s and t we hahve to return ttrue if each strings are anagram of each other else false
        #here for DS we can take a set and from that one set we can go from annother string and then we can remove from that one set and if set is empty thren we can return True or else false 
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char,0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False

            count[char] -= 1    

        return True




            