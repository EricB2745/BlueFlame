from Db.DataClass import DataClass
from Db.Color import Color


class ColorTime(DataClass):
    def __init__(self, id, colorid, startdatetime, enddatetime, status):
        DataClass.__init__(self)

        self.id = id
        self.colorid = colorid
        self.startdatetime = startdatetime
        self.enddatetime = enddatetime
        self.status = status

        self.color = Color(0, '', '', '', '')

    def load(self):
        row = DataClass.selectSproc(self, "Color_Time_Get", "One", str(self.id))

        self.colorid = row[1]
        self.startdatetime = str(row[5])
        self.enddatetime = str(row[6])
        self.status = row[7]

        color = Color(self.colorid, '', '', '', '')
        color.load()
        self.color = color


    def save(self):
        params = "'" + self.colorid + "'"
        params += ",'" + self.startdatetime + "'"
        params += ",'" + self.enddatetime + "'"
        params += ",'" + self.status + "'"

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Color_Time_Insert", "One", params)
            self.id = row[0]
        else:
            # update
            params = str(self.id) + "," + params
            DataClass.executeSproc(self, "Color_Time_Update", params)

    def delete(self):
        DataClass.executeSproc(self, "Color_Time_Delete", str(self.id))

    def toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):

        self._Json = DataClass._toJson(self, jsonHeader, openingBrace, asArray, False)

        self._Json += ","

        self._Json += self.color.toJson('Color', False, False, False)

        self._Json += '}}'

        if asArray == True:
            self._Json += "]"

        if closeJson == True:
            self._Json += "}"

        return self._Json
