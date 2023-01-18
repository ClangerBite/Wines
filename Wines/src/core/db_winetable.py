import sqlite3

from .datastructures import Wine
from .directorymanager import dbase_folder, directory


class WineDBTable:
    def __init__(self):
        with directory(dbase_folder):
            self.connection = sqlite3.connect(":memory:")
            self.cursor = self.connection.cursor()

        wine1 = Wine(
            # "W0001",
            "Chateau Gloria",
            "Red",
            "France",
            "Bordeaux",
            "Paulliac",
            "Cab Sav",
        )
        wine2 = Wine(
            # "W0002",
            "Chateau Margaux",
            "White",
            "France",
            "Bordeaux",
            "St Julien",
            "Cab Sav",
        )

        self.create_wine_table()

        self.insert_record(wine1)
        self.insert_record(wine2)
        wines = self.fetch_by_colour("Red")
        print("Fetch reds")
        for wine in wines:
            print(wine)
        print("*" * 15)

        self.update_colour(1, "Blue")
        wines = self.fetch_by_colour("Blue")
        print("Colour change")
        for wine in wines:
            print(wine)
        print("*" * 15)

        wines = self.fetch_by_country_and_name_and_reverse_colour_order("France")
        print(
            "Name and reverse colour order"
        )  # No need for sort index in transactions application?
        for wine in wines:
            print(wine)
        print("*" * 15)

        print("Print all rows")
        self.print_DB_rows()
        print("*" * 15)

        self.delete_record(1)
        # Best to use rowid if you are deleting or updating a record - this is its unique identifier - no need to wineID etc
        print("Deleted record 1 - reprint all rows")
        self.print_DB_rows()
        print("*" * 15)

        wines = self.fetch_by_colour("White")
        print("Fetch whites")
        for wine in wines:
            print(wine)
        print("*" * 15)

    def create_wine_table(self):
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
        # 5 Datatypes - null (has a null value); integer; real; text; blob (stored exactly as input - eg pictures, audio, etc)

    def execute(self, sql, param=None):
        with self.connection:
            if param != None:
                self.cursor.execute(sql, param)
            else:
                self.cursor.execute(sql)
        return self.cursor.fetchall()
        # NB fetchone() for next row or fetchmany(X) for X rows

    def insert_record(
        self, wine
    ):  # Can also pass over a list of wines and use 'executemany' with the parameter being the list - do a function for this to read from excel spreadsheet
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

    def fetch_by_colour(self, colour):
        sql = "SELECT * FROM wines WHERE colour = :colour"
        # Can add more by using AND or OR afterwards | can also use LIKE with % as asterisk - eg name LIKE 'Ch%' or LIKE '%gmail.com' or date < xxx - use brackets if combining AND + OR
        param = {"colour": colour}
        return self.execute(sql, param)

    def fetch_by_country_and_name_and_reverse_colour_order(self, country):
        sql = "SELECT * FROM wines WHERE country = :country ORDER BY name ASC, colour DESC"
        param = {"country": country}
        return self.execute(sql, param)

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
