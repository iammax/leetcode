class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        numwords = len(sentence.split())
        lensearch = len(searchWord)
        for wordcount in range (numwords):
            thisword = sentence.split()[wordcount]
            
            if len(thisword) < lensearch:
                pass
            else:
                
                if searchWord == thisword[:lensearch]:
                    return wordcount+1
        return -1 
