
import MySQLdb


class DataClass(object):
    def __init__(self):
        f = open('db.config', 'r')
        self.__ip = f.readline().rstrip('\n')
        self.__uid = f.readline().rstrip('\n')
        self.__pwd = f.readline().rstrip('\n')
        self.__schema = f.readline().rstrip('\n')


    def __connectDb(self):
        # Open database connection
        self.__db = MySQLdb.connect(self.__ip, self.__uid, self.__pwd, self.__schema)


    def selectSproc(self, sproc, returnType, params):
        self.__connectDb()

        # prepare a cursor object using cursor() method
        cursor = self.__db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "CALL "+sproc+"("+params+");"

        # Execute the SQL command
        cursor.execute(sql)

        if returnType == 'All':
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        else:
            results = cursor.fetchone()

        return results

        # close cursor
        cursor.close()

        self.__db.close()


    def executeSproc(self, sproc, params):
        self.__connectDb()

        # prepare a cursor object using cursor() method
        cursor = self.__db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "CALL "+sproc+"("+params+");"

        # Execute the SQL command
        cursor.execute(sql)

        # close cursor
        cursor.close()

        self.__db.close()


    def _toJson(self, jsonHeader='Self', openingBrace=True, asArray=False, closeJson=True):
        # This function has the ability to return the members of the derived class as JSON
        # It can return several derviatives of the json based on parameters
        #
        # jsonHeader drives how the header is represented.  Default is self meaning using class name
        # closJson is a flag that indicates if the function should append closing braces.  this is set to false
        # the calling function wants to add more Json to the json
        #
        # sample JSON
        # {"menu": {
        #     "id": "file",
        #     "value": "File",
        #    "popup": {
        #        "menuitem": [
        #             {"value": "New", "onclick": "CreateNewDoc()"},
        #            {"value": "Open", "onclick": "OpenDoc()"},
        #             {"value": "Close", "onclick": "CloseDoc()"}
        #         ]
        #    }
        # }


        self._Json = ''

        if openingBrace == True:
            self._Json += '{'

            # Prefix JSON with class name
        if jsonHeader == 'Self':
            self._Json += self.__class__.__name__ + '":'
            #self._Json += '{"data":'
        elif jsonHeader != 'None':
            self._Json += '"' + jsonHeader + '":'

        if asArray==True:
            self._Json += "["

        self._Json += '{ '

        # Format key/values into JSON while ignoring private attributes that start with an underscore
        for k in self.__dict__.keys():
            if not k.startswith('_'):
                # add value to return string
                if type(self.__dict__[k]) == int or type(self.__dict__[k]) == long or type(self.__dict__[k]) == float:
                    # add key to return string
                    self._Json += '"' + k + '":'
                    self._Json += '"' + str(self.__dict__[k]) + '",'
                elif type(self.__dict__[k]) == str:
                    # add key to return string
                    self._Json += '"' + k + '":'
                    self._Json += '"' + self.__dict__[k] + '",'

        #Trim trailing comma
        self._Json = self._Json[:-1]

        if closeJson==True:
            #Close JSON
            self._Json += "}"
            if asArray == True:
                self._Json += "]"
            if openingBrace == True:
                self._Json += "}"

        return self._Json