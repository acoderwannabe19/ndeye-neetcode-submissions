class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        l = len(s)
        max_length = 0
        current_set = set()

        while end < l:
            while s[end] in current_set:
                current_set.remove(s[start])
                start+=1
            
            current_set.add(s[end])
            max_length = max(max_length, end - start + 1)
            end+=1
        
        return max_length

        