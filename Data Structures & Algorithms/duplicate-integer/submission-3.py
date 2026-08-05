class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

#First understand the problem

#Here we have given a numbs array and we have to return true if any value contains more than once in the array or else return the false 
#here we need a quick lookup in array so we have one option which is hashSet()

        contains = set()

        #we take the set contains where we append the values into it and check if cpontains duplicate we will return the true

        for num in nums:
            if num in contains:
                return True

            contains.add(num)

        return False         