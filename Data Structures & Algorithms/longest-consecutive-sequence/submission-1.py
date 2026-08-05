class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        #nums = [2,20,4,10,3,4,5]
        longest_subss = 0
        #0 #1

        for n in nums:
            #2 #20 
            if (n-1) not in hashSet:
                #True True
                length = 0
                #0 1 
                while (n + length) in hashSet:
                    #2+0 = 2
                    length += 1
                    #length 1
                longest_subss = max(longest_subss, length)
                #0,1 = 1
        return longest_subss            


