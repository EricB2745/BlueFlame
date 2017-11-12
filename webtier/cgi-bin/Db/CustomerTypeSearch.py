
from Db.DataClass import DataClass
from Db.CustomerType import CustomerType

class CustomerTypeSearch(DataClass):

    def __init__(self, status):
        DataClass.__init__(self)
        self.status = status

    def search(self):
        params = "'" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Customer_Type_Search", "All", params)

    def toJson(self):
        self.Json = '{ "CustomerTypes" : [ '
        for row in self.rows:
            customerType = CustomerType(row[0], '', '')
            customerType.load()
            self.Json += customerType.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
