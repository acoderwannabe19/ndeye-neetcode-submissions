class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        
        freq_s1 = {}
        for ch in s1:
            freq_s1[ch] = freq_s1.get(ch, 0) + 1
        
        # Slide a window of size l1 over s2
        for i in range(l2 - l1 + 1):
            substring = s2[i:i + l1]
            freq_substring = {}
            for ch in substring:
                freq_substring[ch] = freq_substring.get(ch, 0) + 1
            
            if freq_s1 == freq_substring:
                return True
        
        return False
            