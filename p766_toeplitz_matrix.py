class Solution(object):
    def isToeplitzMatrix(self, matrix):
        ydim = len(matrix)
        xdim = len(matrix[0])
        for y in range (ydim):
            root = matrix[y][0]
            ycount = y+1
            counter = 1
            done = False
            while not done:
                try:
                    here = matrix[ycount][counter]
                    if here != root:
                        
                        return False
                    ycount += 1
                    counter += 1
                except:
                    done = True
        for x in range (1, xdim):
            root = matrix[0][x]
            xcount = x+1
            counter = 1
            done = False
            while not done:
                try:
                    here = matrix[counter][xcount]
                    if here != root:
                        return False
                    counter += 1
                    xcount += 1
                except:
                    done = True
        return True
