
from Db.DataClass import DataClass

class Customer(DataClass):

    def __init__(self, id, name, custtypeid, priority):
        DataClass.__init__(self)
        self.id = id
        self.name = name
        self.custtypeid = custtypeid
        self.priority = priority

    def load(self):
        row = DataClass.selectSproc(self,"Customer_Get", 'One', str(self.id))

        self.id = row[0]
        self.name = row[1]
        self.custtypeid = row[2]
        self.priority = row[3]
        self.custtype = row[4]

    def save(self):
        params = "'"+self.name+"'"
        params +=","+self.custtypeid
        params += ",'" + self.priority + "'"

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Customer_Insert", "One", params)
            self.id = row[0]
            self.custtype = row[1]
        else:
            # update
            params = str(self.id)+","+params
            row = DataClass.selectSproc(self, "Customer_Update", "One", params)
            self.custtype = row[1]

    def delete(self):
        DataClass.executeSproc(self, "Customer_Delete", str(self.id))

    def toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):
        return DataClass._toJson(self, jsonHeader, openingBrace, asArray, closeJson)
