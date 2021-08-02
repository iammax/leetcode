class Solution(object):
    def largeGroupPositions(self, S):
        outs = []
        dim = len(S)
        counter = 1
        streak = 0
        startpos = 0
        prev = S[0]
        while counter < dim:
            here = S[counter]
            print counter, here, streak, prev
            if here == prev:
                print 'hit at ', counter
                if streak == 0:
                    startpos = counter-1
                streak += 1
            else:
                if streak >= 2:
                    outs.append([startpos, counter-1])
                streak = 0
            prev = here
            counter += 1
        if streak >=2:
            outs.append([startpos, counter-1])
        return outs
            
