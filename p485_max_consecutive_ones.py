class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum = 0
        streak = 0
        for num in nums:
            if num == 1:
                streak += 1
                if streak > maximum: 
                    maximum = streak
            else:
                streak = 0
        return maximum
