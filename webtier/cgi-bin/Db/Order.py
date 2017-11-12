
from Db.DataClass import DataClass
from Db.Customer import Customer
from Db.OrderStatus import OrderStatus

class Order(DataClass):

    def __init__(self, id, ordernum, customerid,orderstatusid,orderdate,duedate,price):
        DataClass.__init__(self)
        self.id = id
        self.ordernum=ordernum
        self.customerid=customerid
        self.orderstatusid=orderstatusid
        self.orderdate=orderdate
        self.duedate=duedate
        self.price=price
        self.customer=Customer(0, '', '', '')
        self.items = []


    def load(self):
        row = DataClass.selectSproc(self,"Order_Get", 'One', str(self.id))

        self.ordernum=row[0]
        self.customerid=row[1]
        self.orderstatusid=row[2]
        self.orderdate=row[3]
        self.duedate=row[4]
        self.createdate=row[5]
        self.price=row[6]

        customer = Customer(self.customerid, '', '', '')
        customer.load()
        self.customer = customer

        orderStatus = OrderStatus(self.orderstatusid, '', '')
        orderStatus.load()
        self.orderStatus = orderStatus

    def save(self):
        params = "'"+self.ordernum+"'"
        params +=","+self.customerid
        params += "," + self.orderstatusid
        params += ",'" + self.orderdate + "'"
        params = "'"+self.duedate+"'"
        params += "," + self.price

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Order_Insert", "One", params)
            self.id = row[0]

        else:
            # update
            params = str(self.id)+","+params
            DataClass.executeSproc(self, "Order_Update", "One", params)


    def delete(self):
        DataClass.executeSproc(self, "Order_Delete", str(self.id))

    def toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):

        self._Json = DataClass._toJson(self, jsonHeader, openingBrace, asArray, False)

        self._Json += ","

        self._Json += self.customer.toJson('Customer', False, False, True)

        self._Json += ","

        self._Json += self.orderStatus.toJson('OrderStatus', False, False, True)

        if asArray==True:
            self._Json += "]"

        self._Json += ', "options": {'



        self._Json += '}'

        if closeJson==True:
            self._Json += "}"

        return self._Json
