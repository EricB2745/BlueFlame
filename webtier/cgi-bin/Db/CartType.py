
from Db.DataClass import DataClass

class CartType(DataClass):

    def __init__(self, id, name, description, status):
        DataClass.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.status = status


    def load(self):
        row = DataClass.selectSproc(self,"Cart_Type_Get", "One", str(self.id))

        self.id = row[0]
        self.name = row[1]
        self.description = row[2]
        self.status = row[3]

    def save(self):
        params = "'"+self.name+"'"
        params +=",'"+ self.description + "'"
        params +=",'"+self.status+"'"

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Cart_Type_Insert", "One", params)
            self.id = row[0]
        else:
            # update
            params = str(self.id)+","+params
            DataClass.executeSproc(self, "Cart_Type_Update", params)

    def delete(self):
        DataClass.executeSproc(self, "Cart_Type_Delete", str(self.id))


    def toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):
        return DataClass._toJson(self, jsonHeader, openingBrace, asArray, closeJson)
