#https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:

        pos=[0,0]

        for move in moves:

            if move == "R":
                pos[0] = pos[0] + 1
            elif move == "L":
                pos[0] = pos[0] - 1
            elif move == "U":
                pos[1] = pos[1] + 1
            elif move == "D":
                pos[1] = pos[1] - 1
            else:
                pos = pos

        if pos == [0,0]:
            return True
        else:
            return False

if __name__ == '__main__':
    moves = "LL"
    print(Solution().judgeCircle(moves))
