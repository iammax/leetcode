class Solution(object):
    def groupThePeople(self, groupSizes):
        thedict = {}
        out = []
        numpeople = len(groupSizes)
        person = 0
        while person < numpeople:
            groupsize = groupSizes[person]
            if groupsize in thedict:
                thedict[groupsize].append(person)
            else:
                thedict[groupsize] = [person]
            person += 1
        for groupsize in thedict:
            people = thedict[groupsize]
            numpeople = len(people)
            person = 0
            group = []
            while person < numpeople:
                group.append(people[person])
                if (person+1)%groupsize == 0:
                    out.append(group)
                    group = []
                person += 1          
        return out
