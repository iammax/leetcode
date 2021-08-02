class Solution(object):
    def countPrimeSetBits(self, L, R):
        def binary(x):
            bitlist = []
            while x > 0:
                bitlist.append(x%2)
                x/=2
            return bitlist[::-1]
        numprime = 0
        for q in range (L, R+1):
            num = bin(q)[2:]
            numones = 0
            for r in num:
                numones += r == '1'
            if numones in [2, 3, 5, 7, 11, 13, 17, 19]:
                numprime += 1
        return numprime
