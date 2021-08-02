class Solution(object):
    def isUgly(self, num):
        if num < 1:
            return False
        elif num == 1:
            return True
        elif num % 2 != 0 and  num %3 != 0 and num %5 != 0:
            return False
        else:
            orig_num = num
            num_2s = 0
            num_3s = 0
            num_5s = 0
            while num % 2 == 0:
                num_2s += 1
                num/= 2
            num = orig_num
            while num % 3 == 0:
                num_3s += 1
                num /= 3
            num = orig_num
            while num % 5 == 0:
                num_5s += 1
                num /= 5
            power_of_60 = 60**(max(num_2s, num_3s, num_5s))
            if power_of_60 % num == 0:
                return True
            else:
                return False
