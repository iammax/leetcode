class Solution(object):
    def modifyString(self, s):
        here = s[0]
        letters = 'abcdefg'
        
        if len(s) == 1:
            return 'a'

        if here != '?':
            out = s[0]
            prev = s[0]
        else:
            nextletter = s[1]
            if nextletter == 'a':
                out = 'b'
                prev = 'b'
            else:
                out = 'a'
                prev = 'a'
        counter = 1
        dim = len(s)
        while counter < dim:
            here = s[counter]
            if here != '?':
                out = out + here
                prev = here        
            else:
                useletter = letters.replace(prev, '')
                if dim - counter > 1:
                    nextletter = s[1+counter]
                    useletter = useletter.replace(nextletter, '')
                out = out + useletter[0]    
                prev = useletter[0]
            counter += 1
        return out 
