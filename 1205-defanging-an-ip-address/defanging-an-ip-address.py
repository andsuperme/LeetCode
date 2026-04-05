class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for c in address:
            if c == '.':
                res = res + "[.]"
            else: 
                res = res + c
        return res