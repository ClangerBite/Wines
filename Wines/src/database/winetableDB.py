from .connectDB import ConnectDB


class WineTableDB(ConnectDB):
    def __init__(self) -> None:
        super().__init__()
        self.create_table_if_not_exist()

    def create_table_if_not_exist(self) -> None:
        sql = """CREATE TABLE IF NOT EXISTS wines (    
                    wineID INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    colour TEXT,
                    country TEXT,
                    region TEXT,
                    subregion TEXT,
                    grapetype TEXT
                )"""
        self.execute(sql)
        # TODO delete region & country, change subregion to subregionID INTEGER, consider whether to leave in dataclass (as can pull queries into it) - create a combined dataclass to hold it all
        # don't need country or region as can include in separate look-up table based on subregion

    def insert(self, wine) -> None:
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

    def delete(self, wineID) -> None:
        sql = "DELETE FROM wines WHERE wineID = :wineID"
        param = {"wineID": wineID}
        self.execute(sql, param)

    def update_colour(self, wineID, colour) -> None:
        sql = "UPDATE wines SET colour = :colour WHERE wineID = :wineID"
        param = {
            "wineID": wineID,
            "colour": colour,
        }
        self.execute(sql, param)

    def print_all_rows(self) -> None:
        sql = "SELECT * FROM wines"
        rows = self.execute(sql)
        for row in rows:
            print(row)
