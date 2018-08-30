class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        ydim = len(matrix)-1
        xdim = len(matrix[0])	
        orig_xdim = len(matrix[0])
        output = []
        xdir = 1
        ydir = 1
        thisone = 1 # 1 = x, y = -1
        thisnum = 0
        while xdim > 0 and ydim > 0:
            if thisone == 1:
                for q in range (1, xdim+1):
                    thisnum += (1*xdir)
                    output.append(thisnum)			
                xdir *= -1
                xdim -= 1
            else:
                for q in range (1, ydim+1):
                    thisnum += (orig_xdim*ydir)
                    output.append(thisnum)
                ydir *= -1
                ydim -= 1
            thisone *= -1
        if xdim > 0:
            for q in range (1, xdim+1):
                    thisnum += (1*xdir)
                    output.append(thisnum)	
        elif ydim > 0:
            for q in range (1, ydim+1):
                    thisnum += (orig_xdim*ydir)
                    output.append(thisnum)
        matrixlist = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrixlist.append(matrix[i][j])
        realoutput = []
        for num in output:
            realoutput.append(matrixlist[num-1])
        return realoutput
