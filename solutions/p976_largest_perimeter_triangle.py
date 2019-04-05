class Solution(object):
    def largestPerimeter(self, A):
        A = sorted(A)
        try:
            while True:
                longest = A[-1]
                second = A[-2]
                third = A[-3]
                if (second + third) > longest:
                    return longest + second + third
                else:
                    A = A[:-1]
        except:
            return 0 
