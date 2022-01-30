class Solution(object):
    def twoSum(self, nums, target):
        length = len
        for i in range(length):
            for j in range(i + 1, length):
                num1 = nums[i]
                num2 = nums[j]
                sum = num1 + num2

                if(sum == target):
                    return [i, j]


        return [0, 0]
        