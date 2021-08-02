class Solution(object):
    def subdomainVisits(self, cpdomains):
        thedict = {}
        
        def dicter(x, td, numvisits):
            if x not in td:
                td[x] = numvisits
            else:
                td[x] += numvisits
            return td
        
        for q in cpdomains:
            splitup = q.split()
            numvisits = int(splitup[0])
            domains = splitup[1].split('.')[:-1]
            kind = splitup[1].split('.')[-1]
            thedict = dicter(kind, thedict, numvisits)
            if len(domains) == 1:
                name = '{0}.{1}'.format(domains[0], kind)
                thedict = dicter(name, thedict, numvisits)
            elif len(domains) == 2:
                name = '{0}.{1}'.format(domains[1], kind)
                thedict = dicter(name, thedict, numvisits)
                secondname = '{0}.{1}.{2}'.format(domains[0], domains[1], kind)
                thedict = dicter(secondname, thedict, numvisits)
        outlist = []
        for q in thedict.keys():
            outlist.append("{0} {1}".format(thedict[q], q))
        return outlist
