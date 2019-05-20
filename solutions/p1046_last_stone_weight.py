class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones = sorted(stones)
            biggest, second = stones[-1], stones[-2]
            if biggest > second:
                print stones[:-2], [biggest-second]
                stones = stones[:-2] + [biggest-second]
            else:
                stones = stones[:-2]
        try:
            return stones[0]
        except:
            return 0
