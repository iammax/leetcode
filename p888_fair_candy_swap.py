class Solution(object):
    def fairCandySwap(self, A, B):
        alicetotal = sum(A) 
        bobtotal = sum(B)  
        gap = bobtotal - alicetotal 
        for candy in A:
            
            newalicetotal = alicetotal - candy
            newbobtotal = bobtotal + candy
            newgap = newbobtotal - newalicetotal
            if newgap > 0:
                if newgap/2 in B:
                    return [candy, newgap/2]
