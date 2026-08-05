class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = []

        for current_index, current_temp in enumerate(temperatures):
            while stack and current_temp > stack[-1][1]:
                previous_index,previous_temp = stack.pop()
                output[previous_index] = current_index - previous_index
            stack.append([current_index,current_temp])

        return output        

        