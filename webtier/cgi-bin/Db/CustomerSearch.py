
from Db.DataClass import DataClass
from Db.Customer import Customer

class CustomerSearch(DataClass):


    def __init__(self, priority):
        DataClass.__init__(self)
        self.priority = priority

    def search(self):
        params = "'" + self.priority + "'"
        self.rows = DataClass.selectSproc(self,"Customer_Search", "All", params)

    def toJson(self):
        self.Json = '{ "Customers" : [ '
        for row in self.rows:
            customer = Customer(row[0], '', '', '')
            customer.load()
            self.Json += customer.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
