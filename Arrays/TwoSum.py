class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        dictionary = {}

        for i in range(length):
            difference = target - nums[i]

            if(not dictionary.get(difference) == None):
                return [dictionary.get(difference), i]
            
            dictionary[nums[i]] = i


        return [0, 0]
        