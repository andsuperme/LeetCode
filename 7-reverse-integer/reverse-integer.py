class Solution:
    def reverse(self, x: int) -> int:
        res = str(x)
        res2 = res[::-1]
        if res2[-1] == '-':
            res2 = "-" + res2[:-1]
        res2 = int(res2)

        if (res2 > 2 **31 - 1 or res2 < -2**31):
            return 0
        return int(res2)