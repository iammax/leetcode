class Solution(object):
    def guessNumber(self, n):
        leftbound = 1
        rightbound = n+1
        while True:
            myguess = (leftbound+rightbound)/2
            result =  guess(myguess)
            if result == 0:
                return myguess
            elif result == 1:
                leftbound = myguess
            elif result == -1:
                rightbound = myguess
