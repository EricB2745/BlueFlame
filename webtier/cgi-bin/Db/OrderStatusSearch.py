
from Db.DataClass import DataClass
from Db.OrderStatus import OrderStatus

class OrderStatusSearch(DataClass):

    def __init__(self, status):
        DataClass.__init__(self)
        self.status = status

    def search(self):
        params = "'" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Order_Status_Search", "All", params)

    def toJson(self):
        self.Json = '{ "OrderStatuses" : [ '
        for row in self.rows:
            orderStatus = OrderStatus(row[0], '', '')
            orderStatus.load()
            self.Json += orderStatus.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
