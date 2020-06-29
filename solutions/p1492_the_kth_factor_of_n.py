class Solution(object):
    def kthFactor(self, n, k):
        count = 0
        for num in range (1, n+1):
            if n % num == 0:
                count += 1
            print num, n % num, count
            if count == k:
                return num
        return -1
