class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        next_non_duplicate_num_place = 0
        prev_number = nums[0]
        for i in range(length):
            curr_num = nums[i]
            if curr_num != prev_number:
                next_non_duplicate_num_place += 1
                nums[next_non_duplicate_num_place] = curr_num
                prev_number = curr_num
        
        return next_non_duplicate_num_place + 1
            