import sqlite3

from .directorymanager import directory, dbase_folder, dbase_name


class QueryDataBase:
    def __init__(self):
        with directory(dbase_folder):
            self.connection = sqlite3.connect(dbase_name)
            self.cursor = self.connection.cursor()

    def execute(self, sql, param=None):
        with self.connection:
            if param != None:
                self.cursor.execute(sql, param)
            else:
                self.cursor.execute(sql)
        return self.cursor.fetchall()
        # NB fetchone() for next row or fetchmany(X) for X rows

    def fetch_by_colour(self, colour):
        sql = "SELECT * FROM wines WHERE colour = :colour"
        # Can add more by using AND or OR afterwards | can also use LIKE with % as asterisk - eg name LIKE 'Ch%' or LIKE '%gmail.com' or date < xxx - use brackets if combining AND + OR
        param = {"colour": colour}
        return self.execute(sql, param)

    def fetch_by_country_and_name_and_reverse_colour_order(self, country):
        sql = "SELECT * FROM wines WHERE country = :country ORDER BY name ASC, colour DESC"
        param = {"country": country}
        return self.execute(sql, param)

    def __close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def __del__(self):
        self.__close()
