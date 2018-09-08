class Solution(object):
    def complexNumberMultiply(self, a, b):
        a1, b1 = parser(a)
        a2, b2 = parser(b)
        outa = (a1*a2)-(b1*b2)
        outb = (a1*b2)+(b1*a2)
        out = str(outa)+'+' + str(outb) + 'i'
        return out
        

def parser(z):
    a = ''
    b = ''
    dim = len(z)
    counter = 0
    mode = 1
    while counter < dim:
        here = z[counter]
        if mode == 1:
            if here != '+':
                a += here
            else:
                mode = 2
                if z[counter+1] == '-':
                    b += '-'
                    counter += 1
        else:
            if here != 'i':
                b += here
        counter += 1
    return [int(a), int(b)]
