class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        #bad brute force solution
        count = 0
        for q in range (1,1+min(a, b)):
            if a%q==0 and b%q == 0:
                count += 1
        return count
