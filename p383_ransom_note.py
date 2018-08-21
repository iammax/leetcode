class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magdict = {}
        for char in magazine:
            if char in magdict:
                magdict[char] += 1
            else:
                magdict[char] = 1
        for char in ransomNote:
            if char in magdict:
                if magdict[char] > 0:
                    magdict[char] -= 1
                else:
                    return False
            else:
                return False
        return True
