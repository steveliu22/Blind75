class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        length = len(nums)
        pointer_one = 0
        pointer_two = length - 1
        squared = [None] * length
        curr_place = length - 1

        for i in range(length):
            nums[i] = nums[i] * nums[i]

        while pointer_one <= pointer_two:
            num_at_pointer_one = nums[pointer_one]
            num_at_pointer_two = nums[pointer_two]

            if num_at_pointer_one >= num_at_pointer_two:
                squared[curr_place] = nums[pointer_one]
                pointer_one += 1
            else:
                squared[curr_place] = nums[pointer_two]
                pointer_two -= 1

            curr_place -= 1

        return squared 