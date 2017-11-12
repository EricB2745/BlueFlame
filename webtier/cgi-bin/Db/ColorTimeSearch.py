

from Db.DataClass import DataClass
from Db.ColorTime import ColorTime

class ColorTimeSearch(DataClass):


    def __init__(self, startdatetime, enddatetime, status):
        DataClass.__init__(self)
        self.startdatetime = startdatetime
        self.enddatetime = enddatetime
        self.status = status

    def search(self):
        params = "'" + self.startdatetime + "','" + self.enddatetime + "','" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Color_Time_Search", "All", params)

    def toJson(self):
        self.Json = '{ "ColorTimes" : [ '
        for row in self.rows:
            colorTime = ColorTime(row[0], '', '', '', '')
            colorTime.load()
            self.Json += colorTime.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json

    def toJsonForCalendar(self):
        self.Json = '['
        for row in self.rows:
            self.Json += '{'
            self.Json += '"id":"'+str(row[0])+'",'
            self.Json += '"colorid":"'+str(row[1])+'",'
            self.Json += '"color":"' + row[3] + '",'
            self.Json += '"start":"' + str(row[5]) + '",'
            self.Json += '"end":"' + str(row[6]) + '"'
            self.Json += '},'

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']'

        return self.Json