class Solution(object):
    def reformatDate(self, date):
        day, month, year = date.split()
        monthdict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        if len(day) == 3:
            day = "0" + day[0]
        else:
            day = day[0:2]
        month = monthdict[month]
        return "{0}-{1}-{2}".format(year, month, day)
