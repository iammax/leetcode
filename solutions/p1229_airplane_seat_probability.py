class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        if n == 1:
            return 1
        else:
            return .5
        
#math explanation... person 1 has probably to be in their own seat with 1/n (100% success) and person n's seat with 1/n (0% success) and a different seat (say seat X) with (n-2)/n. Success rate in that case... seat X can be in seat 1's seat with probability 1/(n-1) (100% success), seat N's seat with 1/(n-1) (0% success), and a different seat (say seat Y) with probability (n-3)/(n-1). Probability ends up recurring until there aren't any seats left. Add them up and you surprisingly always get .5 if n > 1
