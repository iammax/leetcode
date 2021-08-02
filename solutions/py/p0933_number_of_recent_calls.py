class RecentCounter(object):

    def __init__(self):
        self.counter = 0
        self.pings = []

    def ping(self, t):
        self.pings.append(t)
        found = False
        counter = 0
        while not found:
            here = self.pings[counter]
            gap = t - here
            if gap  <= 3000:
                self.pings = self.pings[counter:]
                return len(self.pings) 

            counter += 1
