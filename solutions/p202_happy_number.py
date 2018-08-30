class Solution(object):
    def isHappy(self, n):
        tl = []
        num = n
        while True:
            nextone = adder(num)
            if nextone not in tl:
                tl.append(nextone)
            else:
                if nextone != 1:
                    return False
            if nextone == 1:
                return True
            num = nextone
        
def digits(x):
    out = []
    while x > 0:
        out.append(x%10)
        x/=10
    return out
def adder(y):
    digs = digits(y)
    total = 0
    for q in digs:
        total += q**2
    return total
