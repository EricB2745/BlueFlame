
from Db.DataClass import DataClass
from Db.CartType import CartType

class CartTypeSearch(DataClass):

    def __init__(self, status):
        DataClass.__init__(self)
        self.status = status

    def search(self):
        params = "'" + self.status + "'"
        self.rows = DataClass.selectSproc(self,"Cart_Type_Search", "All", params)

    def toJson(self):
        self.Json = '{ "CartTypes" : [ '
        for row in self.rows:
            cartType = CartType(row[0], '', '', '')
            cartType.load()
            self.Json += cartType.toJson('None', False, False, True) + ','

        #Trim trailing comma
        self.Json = self.Json[:-1]

        #Close JSON
        self.Json += ']}'

        return self.Json
