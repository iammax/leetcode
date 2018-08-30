class Solution(object): #solutition doesn't really update board in place properly, refine this later
    def gameOfLife(self, board):
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        ydim = len(board)
        xdim = len(board[0])
        y = 0
        newboard = []
        while y < ydim:
            newrow = []
            x = 0
            while x < xdim:
                numones = 0
                for direction in directions:
                    yneighbor = y + direction[0]
                    xneighbor = x + direction[1]
                    if xneighbor != -1 and xneighbor != xdim and yneighbor != -1 and yneighbor != ydim:
                        numones += board[yneighbor][xneighbor]
                if board[y][x]: # if alive:
                    if numones == 2 or numones == 3:
                        newrow.append(1)
                    else:
                        newrow.append(0)
                else:
                    if numones == 3:
                        newrow.append(1)
                    else:
                        newrow.append(0)
                x += 1
            newboard.append(newrow)
            y += 1
        for y in range (0, ydim):
            for x in range (0, xdim):
                board[y][x] = newboard[y][x]
