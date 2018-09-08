class Solution(object):
    def complexNumberMultiply(self, a, b):
        a1, b1 = map(int,a[:-1].split('+'))
        a2, b2 = map(int,b[:-1].split('+'))
        outa = (a1*a2)-(b1*b2)
        outb = (a1*b2)+(b1*a2)
        out = str(outa)+'+' + str(outb) + 'i'
        return out
