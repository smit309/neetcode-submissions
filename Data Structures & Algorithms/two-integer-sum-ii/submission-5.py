class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for num in range(len(numbers)):

            need = target - numbers[num]
            if need in seen:
                return [seen[need], num + 1]
                
            seen[numbers[num]] = num + 1    