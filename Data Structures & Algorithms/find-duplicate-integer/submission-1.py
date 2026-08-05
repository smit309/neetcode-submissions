class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        storage = set()

        for num in nums: 
            if num in storage:
                return num
            storage.add(num)    