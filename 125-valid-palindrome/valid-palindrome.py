class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        res = []

        for i in range(len(s)):
            if s[i].lower() in alpha:
                res.append(s[i].lower())
        return res == res[::-1]