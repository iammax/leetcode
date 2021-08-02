class Solution(object):
    def defangIPaddr(self, address):
        #cheat python answer
        #return address.replace('.', '[.]')
        
        #slower but more pure answer
        out = ''
        for q in address:
            if q == '.':
                out += '[.]'
            else:
                out += q
        return out
                
