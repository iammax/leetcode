class Solution(object):
    def judgeCircle(self, moves):
        xpos = 0
        ypos = 0
        if moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D'):
            return True
        return False
