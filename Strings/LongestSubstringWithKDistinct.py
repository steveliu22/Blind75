def getLengthofLongestSubstring(s, k):
    length = len(s)
    seen = {}
    window_start = 0
    num_distinct_characters = 0
    largest_length = 0
    for i in range(length):
        curr_char = s[i]
        
        if seen.get(curr_char) == None or seen.get(curr_char) == 0:
            seen[curr_char] = 1
            num_distinct_characters += 1
        
        while num_distinct_characters > k:
            curr_window_char = s[window_start]
            new_num = seen.get(curr_window_char) - 1
            seen[curr_window_char] = new_num
            if new_num == 0 :
                num_distinct_characters -= 1
            window_start += 1
        
        curr_len = i - window_start + 1

        if curr_len > largest_length:
            largest_length = curr_len

    return largest_length
        
print(getLengthofLongestSubstring("", 3))
