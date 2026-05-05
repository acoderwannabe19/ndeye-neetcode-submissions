class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        i = 0
        while i < len(s):
            # Find the position of the next '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length
        return res