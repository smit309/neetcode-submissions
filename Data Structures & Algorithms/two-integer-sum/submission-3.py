class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for num in range(len(nums)):
            need = target - nums[num]
            if need in output:
                return [output[need], num]

            output[nums[num]] = num  