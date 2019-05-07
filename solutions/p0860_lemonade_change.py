class Solution(object):
    def lemonadeChange(self, bills):
        num5s = 0
        num10s = 0
        for q in range (0, len(bills)):
            #print "5, 10, 20 on hand: {0} {1}, customer is giving: {2}".format(num5s, num10s, bills[q])
            if bills[q] == 5:
                num5s += 1
            elif bills[q] == 10:
                if num5s >= 1:
                    #print 'giving back a 5'
                    num5s -= 1
                    num10s += 1
                else:
                    #print 'no change for a 10'
                    return False
            elif bills[q] == 20:
                if num5s > 0 and num10s > 0:
                    #print 'giving back a 5 and a 10'
                    num5s -= 1 
                    num10s -= 1
                elif num5s > 2:
                    #print 'giving back three 5s'
                    num5s -= 3
                else:
                    #print 'no change for a 20'
                    return False
        return True
        
