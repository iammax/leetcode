class Solution(object):
    def isPathCrossing(self, path):
        x = 0
        y = 0
        visited = [[0,0]]
        for go in path:
            if go == 'N':
                y += 1
            elif go == 'S':
                y -= 1
            elif go == 'W':
                x -= 1
            elif go == 'E':
                x += 1
            
            if [x, y] in visited:
                return 1
            
            else:
                visited = visited + [[x,y]]
            
        return 0
