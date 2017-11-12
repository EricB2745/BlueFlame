
from Db.DataClass import DataClass

class Color(DataClass):

    def __init__(self, id, code, description, hexcode, status):
        DataClass.__init__(self)
        self.id = id
        self.code = code
        self.description = description
        self.hexcode = hexcode
        self.status = status


    def load(self):
        row = DataClass.selectSproc(self,"Color_Get", "One", str(self.id))

        self.code = row[1]
        self.description = row[2]
        self.hexcode = row[3]
        self.status = row[4]

    def save(self):
        params = "'"+self.code+"'"
        params +=",'"+ self.description + "'"
        params +=",'"+ self.hexcode + "'"
        params +=",'"+self.status+"'"

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Color_Insert", "One", params)
            self.id = row[0]
        else:
            # update
            params = str(self.id)+","+params
            DataClass.executeSproc(self, "Color_Update", params)

    def delete(self):
        DataClass.executeSproc(self, "Color_Delete", str(self.id))


    def toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):
        return DataClass._toJson(self, jsonHeader, openingBrace, asArray, closeJson)
