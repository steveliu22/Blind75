class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)

        if(length == 1):
            return 0

        prefix = [0] * length
        suffix = [0] * length
        ans = [0] * length
        backwards = length - 1
        curr_prefix = nums[0]
        curr_suffix = nums[backwards]
        
        for i in range(length - 1):
            prefix[i] = curr_prefix
            suffix[backwards] = curr_suffix
            curr_prefix = curr_prefix * nums[i + 1]
            curr_suffix = curr_suffix * nums[backwards - 1]
            backwards = backwards - 1

        prefix[length - 1] = curr_prefix
        suffix[0] = curr_suffix

        for j in range(length):
            if j == 0:
                ans[0] = suffix[1]
            
            elif j == length - 1:
                ans[length - 1] = prefix[length - 2]
            
            else:
                ans[j] = prefix[j - 1] * suffix[j + 1]

        return ans


        