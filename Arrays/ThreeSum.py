class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        length = len(nums)
        seen = {}
        index = 0
        solution = []

        if length < 3:
            return []

        nums.sort()

        while index < length:

            if seen.get(nums[index]) != None :
                index += 1
                continue

            
            right = length - 1
            left = index + 1
            target = -1 * nums[index]
            seen[nums[index]] = index
            while left < right:

                left_num = nums[left]
                right_num = nums[right]
                sum = left_num + right_num

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    solution.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                

            
            index += 1
        
        return solution

            


