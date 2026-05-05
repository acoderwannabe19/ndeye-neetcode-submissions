class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            # Sort the word to get the anagram key
            key = "".join(sorted(word))  # e.g. "eat" -> ('a', 'e', 't')

            # Group words by the same sorted key
            if key in hash_map:
                hash_map[key].append(word)
            else:
                hash_map[key] = [word]

        # Collect grouped anagrams
        result = list(hash_map.values())
        return result