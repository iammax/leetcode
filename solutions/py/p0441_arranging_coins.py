class Solution(object):
    def arrangeCoins(self, n):
        x = 0
        while True:
            if triangle(x) == n:
                return x
            elif triangle(x) > n:
                return x-1
            x += 1
        
        
def triangle(x):
    return (x**2 + x)/2
