class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Create two frequency dictionaries
        freq_s = {}
        freq_t = {}

        # Count frequency of each character in s
        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1

        # Count frequency of each character in t
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1

        # Compare the two dictionaries
        return freq_s == freq_t
        