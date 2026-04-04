class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num % 3 != 0:
                res = res + 1
            print (res)
        return res