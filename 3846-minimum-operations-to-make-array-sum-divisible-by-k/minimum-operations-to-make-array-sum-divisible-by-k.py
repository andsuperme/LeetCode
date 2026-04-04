class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(num for num in nums)

        return total % k