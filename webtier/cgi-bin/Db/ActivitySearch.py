
from Db.DataClass import DataClass
from Db.Activity import Activity

class ActivitySearch(DataClass):

    def __init__(self, status):
        DataClass.__init__(self)
        self.status = status

    def search(self):
        params = "'" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Activity_Search", "All", params)

    def toJson(self):
        self.Json = '{ "Activities" : [ '
        for row in self.rows:
            cartType = Activity(row[0], '', '', '')
            cartType.load()
            self.Json += cartType.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
