class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr = sorted(arr)
        prev = arr[1]
        prevgap = arr[1] - arr[0]
        for num in arr[2:]:
            if num - prev != prevgap:
                return False
            prev = num
        return True
