class Solution(object):
    def checkPerfectNumber(self, num):
        def root_checker(num):
            if num == 1:
                return 0
            total = 1
            for q in range (2,1+ int(num**.5)):
                if num%q == 0:
                    total += q
                    quo = num/q
                    if q != quo:
                        total += quo
            return total
        if num < 6:
            return False
        elif num == root_checker(num):
            return True
        else:
            return False
