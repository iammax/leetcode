class Solution(object):
    def getHint(self, secret, guess):
        secretlist = [q for q in secret]
        print secretlist
        dim = len(secret)
        counter = 0
        bulls = 0
        cows = 0
        while counter < dim:
            this_guess  = guess[counter]
            this_secret = secret[counter]
            if this_guess == this_secret:
                bulls += 1
                try:
                    secretlist.remove(this_secret)
                except:
                    cows -= 1
            else:
                if this_guess in secretlist:
                    cows += 1
                    secretlist.remove(this_guess)
            counter += 1
        return '{0}A{1}B'.format(bulls, cows)
