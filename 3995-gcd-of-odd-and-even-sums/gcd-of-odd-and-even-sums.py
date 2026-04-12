class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n == 1:
            return n
        
        mostOdd = (n * 2) - 1
        mostEven = n * 2

        sumOfOdd = (1 + mostOdd) * n / 2
        sumOfEven = (2 + mostEven) * n / 2

        for i in range(n * 2, 1, -1):
            if sumOfOdd % i == 0 and sumOfEven % i == 0:
                return i