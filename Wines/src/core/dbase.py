import sqlite3

from .datastructures import Wine


class WineDB:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        wine1 = Wine(
            "W0001",
            "Chateau Gloria",
            "Red",
            "France",
            "Bordeaux",
            "Paulliac",
            "Cab Sav",
        )
        wine2 = Wine(
            "W0002",
            "Chateau Margaux",
            "Red",
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

        self.update_colour(wine1, "Blue")
        wines = self.fetch_by_colour("Blue")
        print("Colour change")
        for wine in wines:
            print(wine)
        print("*" * 15)

        print("Print all rows")
        self.print_DB_rows()
        print("*" * 15)

        self.delete_record(wine1)
        wines = self.fetch_by_colour("Red")
        print("Fetch reds")
        for wine in wines:
            print(wine)
        print("*" * 15)

    def create_wine_table(self):
        
        table_name= "wines"
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name = :table"
        param = {"table": table_name}
        table_exists = bool(self.execute(sql, param))
        
        if not table_exists:
            sql = """CREATE TABLE wines (    
                        wineID text,
                        name text,
                        colour text,
                        country text,
                        region text,
                        subregion text,
                        grapetype text
                    )"""
            self.execute(sql)
            print(f"Table '{table_name}' created")        
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

    def insert_record(self, wine):
        sql = "INSERT INTO wines VALUES (:wineID, :name, :colour, :country, :region, :subregion, :grapetype)"
        param = {
            "wineID": wine.wineID,
            "name": wine.name,
            "colour": wine.colour,
            "country": wine.country,
            "region": wine.region,
            "subregion": wine.subregion,
            "grapetype": wine.grapetype,
        }
        self.execute(sql, param)

    def delete_record(self, wine):
        sql = "DELETE from wines WHERE wineID = :wineID"
        param = {"wineID": wine.wineID}
        self.execute(sql, param)

    def update_colour(self, wine, colour):
        sql = "UPDATE wines SET colour = :colour WHERE wineID = :wineID"
        param = {
            "wineID": wine.wineID,
            "colour": colour,
        }
        self.execute(sql, param)

    def fetch_by_colour(self, colour):
        sql = "SELECT * FROM wines WHERE colour = :colour"
        param = {"colour": colour}
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
