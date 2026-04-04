class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hm = {
            "++" : 1,
            "--" : -1,
        }

        total = 0
        for i in range(len(operations)):
            if "++" in operations[i]:
                total += hm["++"]
            else:
                total += hm["--"]
        return total