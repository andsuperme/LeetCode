class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        greatest = 0
        for i in range(len(candies)):
            if candies[i] > greatest:
                greatest = candies[i]
        
        for j in range(len(candies)):
            res.append(candies[j] + extraCandies >= greatest)
        return res
        