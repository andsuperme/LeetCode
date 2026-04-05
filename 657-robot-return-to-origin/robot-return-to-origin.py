class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ver = 0
        hor = 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                ver += 1
            elif moves[i] == 'R':
                hor += 1
            elif moves[i] == 'L':
                hor -= 1
            else:
                ver -= 1
        return ver == 0 and hor == 0 