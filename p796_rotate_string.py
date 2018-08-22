class Solution(object):
    def rotateString(self, A, B):
        dim = len(B)
        orders = []
        if A == '' and B == '':
            return True
        if len(A) != len(B):
            return False
        for q in range (0, dim):
            order = []
            for r in range (0, dim):
                order.append((q+r)%dim)
            orders.append(order)
        for order in orders:
            stri = ''
            for entry in order:
                stri += B[entry]
            if stri == A:
                return True
        return False
