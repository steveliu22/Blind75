class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        length = len(nums)
        for i in range(length):
            val = nums[i]
            attempt = dict.get(val)

            if attempt == None:
                dict[val] = 1

            else:
                return True
        
        return False
