class Solution(object):
    def lastStoneWeight(self, stones):
        stones = sorted(stones)
        while len(stones) > 1:
            biggest, second = stones[-1], stones[-2]
            if biggest > second:
                stones = stones[:-2]
                newstone = biggest - second
                dummy = False
                counter = 0
                while not dummy:
                    try:
                        here = stones[counter]
                        if newstone <= here:
                            stones = stones[:counter] + [newstone] + stones[counter:]
                            dummy = True
                        else:
                            counter += 1
                    
                    except:
                        dummy = True
                        stones = stones + [newstone]
            else:
                stones = stones[:-2]
        try:
            return stones[0]
        except:
            return 0
