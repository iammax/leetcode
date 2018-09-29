class Solution(object):
    def solveEquation(self, equation):
        left, right = equation.split('=')
        leftx, leftnum = doublesplit(left)
        rightx, rightnum = doublesplit(right)
        if rightnum == leftnum:
            if leftx == rightx:
                return "Infinite solutions"
            else:
                return 'x=0'
        leftx -= rightx
        rightnum -= leftnum
        if leftx != 0:
            return 'x={0}'.format(rightnum/leftx)    
        else:
            if rightnum != 0:
                return 'No solution'
            else:
                return "Infinite solutions"
            
def doublesplit(st):
    outnums = []
    outxs = []
    sub = ''
    nextneg = 0
    for q in st:
        if q == 'x':
            if sub != '':
                outxs.append(int(sub))
                sub = ''
            else:
                if nextneg == 1:
                    outxs.append(-1)
                else:
                    outxs.append(1)
            nextneg = 0
        elif q == '+':
            if sub != '':
                outnums.append(int(sub))
                sub = ''
        elif q == '-':
            nextneg = 1
            if sub != '':
                outnums.append(int(sub))
                sub = ''
        else:
            if nextneg == 1:
                sub += '-'
                nextneg = 0
            sub += q
    if sub != '':
        outnums.append(int(sub))
    return sum(outxs), sum(outnums)
            
