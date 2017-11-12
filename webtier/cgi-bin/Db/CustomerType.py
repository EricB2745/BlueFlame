
from Db.DataClass import DataClass

class CustomerType(DataClass):


    def __init__(self, id, description, status):
        DataClass.__init__(self)
        self.id = id
        self.description = description
        self.status = status


    def load(self):
        row = DataClass.selectSproc(self,"Customer_Type_Get", 'One', str(self.id))

        self.id = row[0]
        self.description = row[1]
        self.status = row[2]

    def save(self):
        params = "'"+self.description+"'"
        params +=",'"+self.status+"'"

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Customer_Type_Insert", "One", params)
            self.id = row[0]
        else:
            # update
            params = str(self.id)+","+params
            DataClass.executeSproc(self, "Customer_Type_Update", params)

    def delete(self):
        DataClass.executeSproc(self, "Customer_Type_Delete", str(self.id))


    def toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):
        return DataClass._toJson(self, jsonHeader, openingBrace, asArray, closeJson)
