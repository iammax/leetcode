class Solution(object):
    def longestCommonPrefix(self, strs):
        out = ''
        numwords = len(strs)
        condition = False
        same = 1
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        for thing in strs:
		    if thing == '':
    			return thing
        while same == 1:
            counter = 0
            while counter < numwords-1:
                thisword = strs[counter]
                nextword = strs[counter+1]
                if len(thisword) > 0 and len(nextword) > 0:
                    same *= (thisword[0] == nextword[0])
                else:
                    same = 0
                    
                strs[counter] = strs[counter][1:]
                counter += 1
            if len(strs[-1]) > 0:
                strs[-1] = strs[-1][1:]
            if len(thisword) > 0:
                out += thisword[0]*same
        return out
                
