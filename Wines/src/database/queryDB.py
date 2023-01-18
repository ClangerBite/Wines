from .connectDB import ConnectDB


class QueryDB(ConnectDB):
    def __init__(self) -> None:
        super().__init__()

    def fetch_by_colour(self, colour) -> list:
        sql = "SELECT * FROM wines WHERE colour = :colour"
        # Can add more by using AND or OR afterwards | can also use LIKE with % as asterisk - eg name LIKE 'Ch%' or LIKE '%gmail.com' or date < xxx - use brackets if combining AND + OR
        param = {"colour": colour}
        return self.execute(sql, param)

    def fetch_by_country_and_name_and_reverse_colour_order(self, country) -> list:
        sql = "SELECT * FROM wines WHERE country = :country ORDER BY name ASC, colour DESC"
        param = {"country": country}
        return self.execute(sql, param)
