import sqlite3

from .directorymanager import directory, dbase_folder, dbase_name


class WineDBTable:
    def __init__(self):
        with directory(dbase_folder):
            self.connection = sqlite3.connect(dbase_name)
            self.cursor = self.connection.cursor()

        self.create_table_if_not_exist()

    def create_table_if_not_exist(self):
        sql = """CREATE TABLE IF NOT EXISTS wines (    
                    wineID INTEGER PRIMARY KEY AUTOINCREMENT,
                    name text,
                    colour text,
                    country text,
                    region text,
                    subregion text,
                    grapetype text
                )"""
        self.execute(sql)
        # don't need country or region as can include in separate look-up table based on subregion

    def execute(self, sql, param=None):
        with self.connection:
            if param != None:
                self.cursor.execute(sql, param)
            else:
                self.cursor.execute(sql)
        return self.cursor.fetchall()
        # NB fetchone() for next row or fetchmany(X) for X rows

    def insert_record(self, wine):
        # Can also pass over a list of wines and use 'executemany' with the parameter being the list - do a function for this to read from excel spreadsheet
        sql = "INSERT INTO wines VALUES (:wineID, :name, :colour, :country, :region, :subregion, :grapetype)"
        param = {
            "wineID": None,
            "name": wine.name,
            "colour": wine.colour,
            "country": wine.country,
            "region": wine.region,
            "subregion": wine.subregion,
            "grapetype": wine.grapetype,
        }
        self.execute(sql, param)

    def delete_record(self, wineID):
        sql = "DELETE from wines WHERE wineID = :wineID"
        param = {"wineID": wineID}
        self.execute(sql, param)

    def update_colour(self, wineID, colour):
        sql = "UPDATE wines SET colour = :colour WHERE wineID = :wineID"
        param = {
            "wineID": wineID,
            "colour": colour,
        }
        self.execute(sql, param)

    def print_DB_rows(self):
        sql = "SELECT * FROM wines"
        rows = self.execute(sql)
        for row in rows:
            print(row)

    def __close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def __del__(self):
        self.__close()
