class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        
        for j in stones:
            if j in jewels:
                res += 1
        return res
