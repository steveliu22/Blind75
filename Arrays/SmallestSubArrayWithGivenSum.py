import math

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        length = len(nums)
        starting = 0
        smallest_length = math.inf
        sum = 0

        for i in range(length):
            sum += nums[i]
            while sum >= target:

                curr_length = i - starting + 1
                if curr_length < smallest_length:
                    smallest_length = curr_length
                sum -= nums[starting]
                starting += 1
            
        if smallest_length == math.inf:
            return 0
            
        return smallest_length
