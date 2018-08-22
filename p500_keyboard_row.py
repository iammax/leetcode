class Solution(object):
    def findWords(self, words):
        
        def whichlist(x):
            row1 = ['q','w','e','r','t','y','u','i','o','p', 'Q','W','E','R','T','Y','U','I','O','P']
            row2 = ['a','s','d','f','g','h','j','k','l', 'A','S','D','F','G','H','J','K','L']
            row3 = ['z','x','c','v','b','n','m', 'Z','X','C','V','B','N','M']
            if x in row1:
                dummy = 1
            elif x in row2:
                dummy = 2
            elif x in row3:
                dummy = 3
            
            return dummy
        
        correctlist = []
        for word in words:
            counter = 1
            failed = 0
            dummy = whichlist(word[0])
            length = len(word)
            while failed == 0 and counter < length:
                newone = whichlist(word[counter])
                if newone != dummy:
                    failed = 1
                counter +=1
                dummy = newone
            if failed == 0:
                correctlist.append(word)
        return correctlist
