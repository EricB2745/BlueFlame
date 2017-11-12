
import MySQLdb

class DataClass(object):
    def __init__(self):
        f = open('db.config', 'r')
        self.__ip = f.readline().rstrip('\n')
        self.__uid = f.readline().rstrip('\n')
        self.__pwd = f.readline().rstrip('\n')
        self.__schema = f.readline().rstrip('\n')
        print "DataClass Init"

    def __connectDb(self):
        # Open database connection
        self.__db = MySQLdb.connect(self.__ip, self.__uid, self.__pwd, self.__schema)


    def selectSproc(self, sproc, params):
        self.__connectDb()

        # prepare a cursor object using cursor() method
        cursor = self.__db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "CALL "+sproc+"("+params+");"
        print "Sql:"+sql

        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        row = cursor.fetchone()

        return row

        # close cursor
        cursor.close()

        self.__db.close()


    def executeSproc(self, sproc, params):
        self.__connectDb()

        # prepare a cursor object using cursor() method
        cursor = self.__db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "CALL "+sproc+"("+params+");"
        print "Sql:"+sql

        # Execute the SQL command
        cursor.execute(sql)

        # close cursor
        cursor.close()

        self.__db.close()

