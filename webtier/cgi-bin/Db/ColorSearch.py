
from Db.DataClass import DataClass
from Db.Color import Color

class ColorSearch(DataClass):


    def __init__(self, status):
        DataClass.__init__(self)
        self.status = status

    def search(self):
        params = "'" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Color_Search", "All", params)

    def toJson(self):
        self.Json = '{ "Colors" : [ '
        for row in self.rows:
            color = Color(row[0], '', '', '', '')
            color.load()
            self.Json += color.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
