
from Db.DataClass import DataClass

class OrderItem(DataClass):

    def __init__(self, id, orderid, orderitemstatusid, colorid, carttypeid, quantity, description, specialinstructions,
        qtyofcarts, oversize, priority, requriesmaskorplug, requiressandblasting, priceper, createdate, subtotal):
        DataClass.__init__(self)
        self.id = id
        self.orderid = orderid
        self.orderitemstatusid = orderitemstatusid
        self.orderitemstatus = ""
        self.colorid = colorid
        self.colorcode = ""
        self.colordesc = ""
        self.carttypeid = carttypeid
        self.carttype = ""
        self.quantity = quantity
        self.description = description
        self.specialinstructions = specialinstructions
        self.qtyofcarts = qtyofcarts
        self.oversize = oversize
        self.priority = priority
        self.requriesmaskorplug = requriesmaskorplug
        self.requiressandblasting = requiressandblasting
        self.priceper = priceper
        self.createdate = createdate
        self.subtotal = subtotal


    def load(self):
        row = DataClass.selectSproc(self,"Order_Item_Get", "One", str(self.id))

        self.orderid = row[1]
        self.orderitemstatusid = row[2]
        self.orderitemstatus = row[3]
        self.colorid = row[4]
        self.colorcode = row[5]
        self.colordesc = row[6]
        self.carttypeid = row[7]
        self.carttype = row[8]
        self.quantity = row[9]
        self.description = row[10]
        self.specialinstructions = row[11]
        self.qtyofcarts = row[12]
        self.oversize = row[13]
        self.priority = row[14]
        self.requriesmaskorplug = row[15]
        self.requiressandblasting = row[16]
        self.priceper = str(row[17])
        self.createdate = row[18]
        self.subtotal = str(row[19])

    def save(self):
        params = "'"   + str(self.orderid) +"'"
        params += ",'" + str(self.orderitemstatusid) + "'"
        params += ",'" + str(self.colorid) + "'"
        params += ",'" + str(self.carttypeid) + "'"
        params += ",'" + self.quantity + "'"
        params += ",'" + self.description + "'"
        params += ",'" + self.specialinstructions + "'"
        params += ",'" + str(self.qtyofcarts) + "'"
        params += ",'" + self.oversize + "'"
        params += ",'" + self.priority + "'"
        params += ",'" + self.requriesmaskorplug + "'"
        params += ",'" + self.requiressandblasting + "'"
        params += ",'" + str(self.priceper) + "'"
        params += ",'" + self.createdate + "'"
        params += ",'" + str(self.subtotal)+"'"

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Order_Item_Insert", "One", params)
            self.id = row[0]
        else:
            # update
            params = str(self.id)+","+params
            DataClass.executeSproc(self, "Order_Item_Update", params)

    def delete(self):
        DataClass.executeSproc(self, "Order_Item_Delete", str(self.id))


    def toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):
        return DataClass._toJson(self, jsonHeader, openingBrace, asArray, closeJson)
