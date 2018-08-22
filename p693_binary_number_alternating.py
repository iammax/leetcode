class Solution(object):
    def hasAlternatingBits(self, n):
        bi = bin(n)[2:]
        condition = True
        counter = 0
        #print 'bi: ', bi
        lastbit = 'nothing'
        while condition == True and counter < len(bi):
            thisbit = bi[counter]
         #   print 'thisbit, prevbit: ', thisbit, prevbit
            if thisbit == lastbit:
             #   print 'equal'
                condition = False
            else:
              #  print 'not equal'
                counter += 1
            lastbit = thisbit
        return condition
        
