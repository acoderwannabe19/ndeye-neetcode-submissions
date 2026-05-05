class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        s = s.lower()
        left = 0
        right = len(s) - 1
        mid = (len(s) // 2) - 1
        while(left<=mid and right>=mid):
            if (s[left] != s[right]):
                return False
            left+=1
            right-=1
        return True

        