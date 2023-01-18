from .connectDB import ConnectDB


class RegionTableDB(ConnectDB):
    def __init__(self) -> None:
        super().__init__()
        self.create_table_if_not_exist()

    def create_table_if_not_exist(self) -> None:
        sql = """CREATE TABLE IF NOT EXISTS regions (    
                    wineID INTEGER PRIMARY KEY AUTOINCREMENT,
                    subregion TEXT,
                    region TEXT,
                    country TEXT
                )"""
        self.execute(sql)
        # don't need country or region as can include in separate look-up table based on subregion

    def insert(self, region) -> None:
        # Can also pass over a list of wines and use 'executemany' with the parameter being the list - do a function for this to read from excel spreadsheet
        sql = "INSERT INTO regions VALUES (:regionID, :subregion, :region, :country)"
        param = {
            "regionID": None,
            "subregion": region.subregion,
            "region": region.region,
            "country": region.country,
        }
        self.execute(sql, param)

    def delete(self, regionID) -> None:
        sql = "DELETE FROM regions WHERE regionID = :regionID"
        param = {"regionID": regionID}
        self.execute(sql, param)

    def amend_subregion_spelling(self, oldname, newname) -> None:
        sql = "UPDATE regions SET subregion = :newsubregion WHERE subregion = :oldsubregion"
        param = {"oldsubregion": oldname, "newsubregion": newname}
        self.execute(sql, param)

    def amend_region_spelling(self, oldname, newname) -> None:
        sql = "UPDATE regions SET region = :newregion WHERE region = :oldregion"
        param = {"oldregion": oldname, "newregion": newname}
        self.execute(sql, param)

    def print_all_rows(self) -> None:
        sql = "SELECT * FROM regions"
        rows = self.execute(sql)
        for row in rows:
            print(row)
