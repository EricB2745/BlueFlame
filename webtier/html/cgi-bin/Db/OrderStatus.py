
from Db.DataClass import DataClass

class OrderStatus(DataClass):
    """Data class used to load from or save to a unique row in the database
                Table:  Order_Status

    Attributes:
        id: Int primary key of Order_Status table
        description:  String
                status: Active or Inactive
    """

    def __init__(self, id, description, status):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        DataClass.__init__(self)
        self.id = id
        self.description = description
        self.status = status
        print "Order Status init"


    def load(self):
        row = DataClass.selectSproc(self,"Order_Status_Get", str(self.id))

        self.id = row[0]
        self.description = row[1]
        self.status = row[2]

    def save(self):
        params = "'"+self.description+"'"
        params +=",'"+self.status+"'"

        if self.id < 1:
            # insert
            row = DataClass.selectSproc(self, "Order_Status_Insert", params)
            self.id = row[0]
        else:
            # update
            params = str(self.id)+","+params
            DataClass.executeSproc(self, "Order_Status_Update", params)

    def delete(self):
        DataClass.executeSproc(self, "Order_Status_Delete", str(self.id))