class Solution(object):
    def maximum69Number (self, num):
        strnum = str(num)
        counter = 0
        out = 0
        dim = len(strnum)
        found = 0
        while counter < dim:
            if strnum[counter] == '6':
                if found == 1:
                    out += 6*(10**(dim-counter-1))
                else:
                    out += 9*(10**(dim-counter-1))
                    found = 1
            else:
                out += 9*(10**(dim-counter-1))
            counter += 1
        return out
                
