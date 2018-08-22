class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        
        if n == 0:
            return True
        if flowerbed == [1] and n == 1:
            return False
        if flowerbed == [0] and n == 1:
            return True
        bed = len(flowerbed)
        if bed > 2:
            counter = 1
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n-=1
                flowerbed[0] = 1
            here = flowerbed[0]
            nextone = flowerbed[1]
            while counter < bed-1:
                print n
                prev = flowerbed[counter-1]
                here = flowerbed[counter]
                nextone = flowerbed[counter+1]
                if prev == 0 and here == 0 and nextone == 0:
                    
                    flowerbed[counter] = 1
                    n -=1
                counter += 1
                if n == 0:
                    return True
        if flowerbed[bed-1] == 0 and flowerbed[bed-2] == 0:
            n -=1 
        return n == 0
            
