oosetwo(x):
    return fact(x)/(2*fact(x-2))
def fact(x):
    if x < 2:
        return 1
    else:
        return x*fact(x-1)    
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        timedict = {0:0, 30:0}
        for song in time:
            modtime = song%60
            if modtime not in timedict:
                timedict[modtime] = 1
            else:
                timedict[modtime] += 1
        total = 0
        for q in range (1, 30):
            if q not in timedict or 60-q not in timedict:
                pass
            else:
                total += timedict[q]*timedict[60-q]
        if timedict[0] > 1: 
            total += choosetwo(timedict[0])
        if timedict[30] > 1:
            total += choosetwo(timedict[30])
        return total
    
        
                
