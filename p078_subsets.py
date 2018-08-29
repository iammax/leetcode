class Solution(object):
    def subsets(self, nums):
        out = []
        dim = len(nums)
        combos = [[0], [1]]
        counter = 1
        while counter < dim:
            newcombos = []
            for combo in combos:
                newyes = combo[:]
                newno = combo[:]
                newyes.append(1)
                newno.append(0)
                newcombos.append(newyes)
                newcombos.append(newno)
            combos = newcombos
            counter += 1
        out = []
        for combo in combos:
            counter = 0
            thisout = []
            while counter <  dim:
                yesno = combo[counter]
                if yesno:
                    thisout.append(nums[counter])
                counter += 1
            out.append(thisout)
        return out
