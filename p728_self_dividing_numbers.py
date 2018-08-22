class Solution(object):
    def selfDividingNumbers(self, left, right):
        yes = []
        for r in range (max(1, left), min(9, right)+1):
            yes.append(r)
        counter = max(11, left)
        while counter <= right:
            if counter % 10 == 0:
                pass
            else:	
                highestpow = len(str(counter))
                subcounter = 1
                div = 1
                while subcounter < highestpow + 1:
                    digit = counter%(10**subcounter)/(10**(subcounter-1))
                    if digit == 0:
                        div = 0
                        subcounter = highestpow + 2
                    else:
                        if counter % digit == 0:
                            subcounter += 1
                        else:
                            div = 0
                            subcounter = highestpow + 2
                if div == 1:
                    yes.append(counter)
            counter += 1
        return yes

