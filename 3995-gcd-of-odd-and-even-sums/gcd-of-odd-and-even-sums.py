class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n == 1:
            return 1
        
        odd = n ** 2
        even = 0

        for i in range(n):
            even += 2
        
        for i in range(even//2, 1, -1):
            if even % i == 0 and odd % i == 0:
                return i