class Solution(object):
    def addDigits(self, num):
        def digits(num):
            digs = []
            while num > 0:
                digs.append(num%10)
                num/=10
            return digs    
        while num >= 10:
            digs = digits(num)
            num = sum(digs)
        return num
