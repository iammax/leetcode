class Solution(object):
    def countBattleships(self, board):
        highest = 0
        ydim = len(board)
        xdim = len(board[0])
        for y in range(ydim):
            for x in range(xdim):
                square = board[y][x]
                if square == 'X':
                    left = '.'
                    up = '.'
                    done = False
                    if x > 0:
                        left = board[y][x-1]
                        if isinstance(left, int):
                            board[y][x] = left                            
                            done = True
                    if y > 0 and not done:
                        up = board[y-1][x]
                        if isinstance(up, int):
                            board[y][x] = up
                            done = True
                    if not done:
                        highest += 1
                        board[y][x] = highest                      
        return highest
