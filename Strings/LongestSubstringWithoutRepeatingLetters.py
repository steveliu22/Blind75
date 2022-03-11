class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index : int = 0
        seen : dict = {}
        max_length : int = 0

        for i in range(len(s)):
            char : str = s[i]
            if seen.get(char) != None:
                if not seen.get(char) + 1 < left_index :
                    left_index = seen.get(char) + 1
            seen[char] = i
            length = 1 + i - left_index
            if length > max_length:
                max_length = length

        return max_length
    
