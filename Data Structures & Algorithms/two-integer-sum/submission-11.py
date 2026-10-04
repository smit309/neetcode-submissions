class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for num in range(len(nums)):
            result = target - nums[num]
            if result in output:
                return [output[result],num]
            output[nums[num]] = num  