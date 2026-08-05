class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #here first we need to return k freq elements
        #first we will count how many times each element appear in the array make sense?
        #Then we traverse from reverse side and will go till the k. values
        #will return the output with top element
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1

        for num,c in count.items(): 
            freq[c].append(num)

        output = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output

            



