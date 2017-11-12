
from Db.DataClass import DataClass
from Db.OrderItemStatus import OrderItemStatus

class OrderItemStatusSearch(DataClass):


    def __init__(self, status):
        DataClass.__init__(self)
        self.status = status

    def search(self):
        params = "'" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Order_Item_Status_Search", "All", params)

    def toJson(self):
        self.Json = '{ "OrderItemStatuses" : [ '
        for row in self.rows:
            orderItemStatus = OrderItemStatus(row[0], '', '')
            orderItemStatus.load()
            self.Json += orderItemStatus.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
