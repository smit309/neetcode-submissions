class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in output:
                return [output[reminder], i]
            output[nums[i]] = i