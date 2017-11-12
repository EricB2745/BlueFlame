
from Db.DataClass import DataClass

class OrderItemSearchByOrderId(DataClass):

    def __init__(self, orderid):
        DataClass.__init__(self)
        self.orderid = orderid

    def search(self):
        params = str(self.orderid)
        self.rows = DataClass.selectSproc(self,"Order_Item_Search_By_Order_Id", "All", params)

    def toJson(self):
        self.Json = '{ "OrderItems" : [ '
        for row in self.rows:
            self.Json += '{'
            self.Json += '"orderitemid":"' + str(row[0]) + '",'
            self.Json += '"orderid":"' + str(row[1]) + '",'
            self.Json += '"orderitemstatusid":"' + str(row[2]) + '",'
            self.Json += '"orderitemstatus":"' + str(row[3]) + '",'
            self.Json += '"colorid":"' + str(row[4]) + '",'
            self.Json += '"colorcode":"' + str(row[5]) + '",'
            self.Json += '"colordesc":"' + str(row[6]) + '",'
            self.Json += '"carttypeid":"' + str(row[7]) + '",'
            self.Json += '"carttype":"' + str(row[8]) + '",'
            self.Json += '"quantity":"' + str(row[9]) + '",'
            self.Json += '"description":"' + str(row[10]) + '",'
            self.Json += '"specialinstructions":"' + str(row[11]) + '",'
            self.Json += '"qtyofcarts":"' + str(row[12]) + '",'
            self.Json += '"oversize":"' + str(row[13]) + '",'
            self.Json += '"priority":"' + str(row[14]) + '",'
            self.Json += '"requriesmaskorplug":"' + str(row[15]) + '",'
            self.Json += '"requiressnadblasting":"' + str(row[16]) + '",'
            self.Json += '"priceper":"' + str(row[17]) + '",'
            self.Json += '"createdate":"' + str(row[18]) + '",'
            self.Json += '"subtotal":"' + str(row[19]) + '"'
            self.Json += '},'

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
