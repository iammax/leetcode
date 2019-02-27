#not pretty but actually beats 100% of submissions for speed as of 2/27/19

class Solution(object):
    def numRookCaptures(self, board):
        counter = 0
        dummy = False
        while not dummy:
            if 'R' in board[counter]:
                y = counter
                dummy = True
            counter += 1
        x = board[counter-1].index('R')
        caps = 0
        dummy = False
        counter = x+1
        while dummy == False and counter < 8:
            here = board[y][counter]
            if here != '.':
                if here == 'p':
                    caps += 1
                dummy = True
            counter += 1
        counter = x-1
        dummy = False
        while dummy == False and counter >= 0:
            here = board[y][counter]
            if here != '.':
                if here == 'p':
                    caps += 1
                dummy = True
            counter -= 1
        counter = y+1
        dummy = False
        while dummy == False and counter < 8:
            here = board[counter][x]
            if here != '.':
                if here == 'p':
                    caps += 1
                dummy = True
            counter += 1
        counter = y-1
        dummy = False
        while dummy == False and counter >= 0:
            here = board[counter][x]
            if here != '.':
                if here == 'p':
                    caps += 1
                dummy = True
            counter -= 1
        
        return caps
