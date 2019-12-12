class Solution(object):
    def subtractProductAndSum(self, n):
        a = str(n)
        prod = 1
        total = 0
        for b in a:
            val = int(b)
            prod *= val
            total += val
        return prod - total
