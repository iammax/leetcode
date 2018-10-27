class Solution(object):
    def isLongPressedName(self, name, typed):
        typedcounter = 0
        namecounter = 0
        namelen = len(name)
        while namecounter < namelen:
            name_letter = name[namecounter]
            print 'name letter: ', name_letter, namecounter
            found = False
            while not found:
                try:
                    typed_letter = typed[typedcounter]
                    print 'typed letter: ', typed_letter, typedcounter
                    if typed_letter == name_letter:
                        found = True
                    typedcounter += 1
                except:
                    return False
            namecounter += 1
        return True
