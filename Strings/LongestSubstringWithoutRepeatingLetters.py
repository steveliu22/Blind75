class Solution:

    #solution to this problem requires the sliding window pattern
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index : int = 0 #starting point of the longest substring
        seen : dict = {} #to keep track of the all of the letters we've seen so far
        max_length : int = 0 #keeps track of the current maximum substring length

        for i in range(len(s)):
            char : str = s[i]
            if seen.get(char) != None: #this means that the current character has been repeated
                #if the character has been repeated but it moves the left index back then we run into the risk of 
                # including other characters that may also have been repeated (ex: dbvxabd, we see that d is repeated at index 6 but if we were to move the left index
                # to the first time the d occurs (at index 1), then we include the b which also has been repeated)
                if seen.get(char) + 1 > left_index : 
                    left_index = seen.get(char) + 1
            seen[char] = i
            length = 1 + i - left_index
            if length > max_length:
                max_length = length

        return max_length
    
