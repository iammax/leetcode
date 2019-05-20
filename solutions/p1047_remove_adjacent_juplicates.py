class Solution(object):
    def removeDuplicates(self, S):
        counter = 1
        nomove = False
        prev = S[0]
        while not nomove:
            if len(S) < 2:
                return S
            if counter > 0:
                here = S[counter]
                if here == prev:
                    try:
                        S = S[:counter-1] + S[counter+1:]
                    except:
                        return S[:counter-1]
                    counter -= 2
                else:
                    counter += 1
                if counter == len(S):
                    nomove = True
                prev = here
            else:
                prev = S[0]
                counter += 1
        return S
