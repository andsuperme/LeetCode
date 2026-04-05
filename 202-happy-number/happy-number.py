class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # track numbers we've already seen to avoid infinite loop
        
        while n != 1:
            if n in seen:
                return False  # cycle detected → not happy
            seen.add(n)
            
            output = 0
            while n > 0:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            n = output  # update n to the sum of squares
        
        return True