#optimized version; beats about 80% on leetcode
class Solution(object):
    def kthFactor(self, n, k):
        
        fronthalf = []
        backhalf = []
        for num in range (1, int(n**.5)+1):
            if n % num == 0:
                
                fronthalf.append(num)
                if n/num != num:
                    backhalf = [n/num] + backhalf
            
        try:
            return (fronthalf + backhalf)[k-1]
        except:
            return -1   

#Below is original, brute force solution, only beats about 10%
#class Solution(object):
#   def kthFactor(self, n, k):
#      count = 0
#     for num in range (1, n+1):
#        if n % num == 0:
#           count += 1
#      print num, n % num, count
#     if count == k:
#        return num
#return -1
