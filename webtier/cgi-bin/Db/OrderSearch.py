
from Db.DataClass import DataClass
from Db.Order import Order

class OrderSearch(DataClass):

    def __init__(self, status):
        DataClass.__init__(self)
        self.status = status

    def search(self):
        params = "'" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Order_Search", "All", params)

    def toJson(self):
        self.Json = '{ "Orders" : [ '
        for row in self.rows:
            self.Json += '{'
            self.Json += '"id":"' + str(row[0]) + '",'
            self.Json += '"order_num":"' + str(row[1]) + '",'
            self.Json += '"customer_id":"' + str(row[2]) + '",'
            self.Json += '"order_status_id":"' + str(row[3]) + '",'
            self.Json += '"order_date":"' + str(row[4]) + '",'
            self.Json += '"due_date":"' + str(row[5]) + '",'
            self.Json += '"create_date":"' + str(row[6]) + '",'
            self.Json += '"price":"' + str(row[7]) + '",'
            self.Json += '"OrderStatus":"' + str(row[8]) + '",'
            self.Json += '"CustomerName":"' + str(row[9]) + '",'
            self.Json += '"CountOfItems":"' + str(row[10]) + '"'
            self.Json += '},'

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
