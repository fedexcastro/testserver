import MySQLdb  # You must install this external package.


class MySQLConnection(object):

    def __init__(self, host, user, pwd, db):
        self.host = host
        self.__db = MySQLdb.connect(host=host, user=user, passwd=pwd, db=db)
        self.__cur = self.__db.cursor()

    def execute(self, sql, commit=False):
        # executes the given sql to the MySQL database
        # might raise errors
        try:
            self.__cur.execute(sql)
            if commit:
                return self.commit()
        except MySQLdb.Error as error:
            try:
                print u"MySQL Error [%d]: %s" % (error.args[0], error.args[1])
            except IndexError:
                print u"MySQL Error: %s" % str(error)
        except Exception as error:
            # Not a good practice, should handle each type of Exception correctly... it's just an idea.
            raise u"Something bad happen executing the query %s.\nError: %s" % (sql, error.message)

    def commit(self):
        try:
            self.__cur.commit()
        except MySQLdb.Error as error:
            print u"Something went wrong when commit.\nError: %s\nRolling back.." % error.message
            self.__db.rollback()
        finally:
            rows = self.__cur.fetchall()
            for row in rows:
                for col in row:
                    print u'%s,' % col

            return rows

    def close(self):
        self.__db.close()