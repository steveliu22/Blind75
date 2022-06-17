class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        length = len(fruits)
        window_start = 0
        max_num_fruits = 0
        number_of_distinct_fruits = 0
        seen = {}
        for i in range(length):
            curr_fruit = fruits[i]

            if seen.get(curr_fruit) == None or seen.get(curr_fruit) == 0:
                seen[curr_fruit] = 1
                number_of_distinct_fruits += 1

            else:
                seen[curr_fruit] = seen.get(curr_fruit) + 1    
            
            while number_of_distinct_fruits > 2:
                curr_window_fruit = fruits[window_start]
                seen[curr_window_fruit] = seen.get(curr_window_fruit) - 1
                if seen.get(curr_window_fruit) == 0:
                    number_of_distinct_fruits -= 1
                window_start += 1
            
            if (i - window_start + 1) > max_num_fruits:
                max_num_fruits = i - window_start + 1

        return max_num_fruits
            
            