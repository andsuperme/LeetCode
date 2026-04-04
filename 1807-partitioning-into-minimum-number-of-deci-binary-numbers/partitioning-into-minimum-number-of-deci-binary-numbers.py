class Solution:
    def minPartitions(self, n: str) -> int:
        highest = 0 


        for d in n:
            part = int(d)
            if part > highest:
                highest = part
        return highest