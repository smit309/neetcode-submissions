class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we have given an array nums and given k value and we have to find a top "k" values from array

        #so suppose there is an array nums[1,2,2,3,3,3] and we have given k = 2 so here 1 comes 1 times, 2 comes 2 times and 3 comes 3 times
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            
            count[num] = count.get(num,0) + 1

        for num, c in count.items():
            freq[c].append(num)

        result = []

        for i in range(len(freq) - 1 , 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result     




