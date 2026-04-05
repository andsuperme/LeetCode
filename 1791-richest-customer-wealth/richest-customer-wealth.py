class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        greatest = 0

        for account in accounts:
            currentBalance = 0
            for i in range(len(account)):
                currentBalance += account[i]
            if currentBalance > greatest:
                greatest = currentBalance
        return greatest
