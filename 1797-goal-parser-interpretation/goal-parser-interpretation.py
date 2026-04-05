class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        left = 0
        while (left < len(command)):
            if command[left] == "(" and command[left + 1] == ")":
                result = result + 'o'
                left += 2
            elif command[left] == "(" and command[left + 1] == "a":
                result = result + "al"
                left += 4
            else: 
                result = result + command[left]
                left += 1
        return result
        
