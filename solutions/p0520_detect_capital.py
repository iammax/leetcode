class Solution(object):
    def detectCapitalUse(self, word):
        caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        smalls = 'abcdefghijklmnopqrstuvwxyz'
        has_smalls = 0
        counter = 0
        dim = len(word)
        capcount = 0
        while counter < dim:
            thisone = word[counter]
            if thisone in caps:
                if has_smalls != 0:
                    return False
                capcount += 1
            elif thisone in smalls and has_smalls == 0:
                has_smalls = 1
            counter += 1
        if capcount < 2:
            return True
        if capcount >= 2 and capcount == dim:
            return True
        else:
            return False
