class Solution(object):
    def tictactoe(self, moves):
        grid = [[0,0,0],[0,0,0],[0,0,0]]
        player = 0
        for move in moves:
            if player%2 == 0:
                grid[move[0]][move[1]] = "X"
            else:
                grid[move[0]][move[1]] = 'O'
                
            player += 1
        print grid
        for row in range (3):
            result = winner(grid[row])
            if result != "N": 
                return result
        for column in range (3):
            col = [grid[0][column],grid[1][column],grid[2][column]]
            result = winner(col)
            if result != "N": 
                return result
        diag1 = [grid[0][0],grid[1][1],grid[2][2]]
        result = winner(diag1)
        if result != "N": 
            return result
        diag2 = [grid[0][2], grid[1][1], grid[2][0]]
        result = winner(diag2)
        if result != "N": 
            return result
        if len(moves) < 9:
            return 'Pending'
        else:
            return "Draw"
        
def winner(row):
    
    if row.count('X') == 3:
                 return "A"
    elif row.count("O") == 3:
                 return "B"
    else:
                 return "N"

