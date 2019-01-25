class Solution(object):
    def fib(self, N):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)
#       If you want to cheat and use the formula which is way faster... use below
        
#       phi = (1 + (5**.5))/2
#       return int((phi**N - (1-phi)**N)/(5**.5))
