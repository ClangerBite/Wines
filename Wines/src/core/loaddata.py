from datetime import datetime

from ..database.queryDB import QueryDB
from ..database.winetableDB import WineTableDB
from .datastructures import Review, Vintage, Websites, Wine

wine1 = Wine(
    "Château Grand-Puy-Lacoste",
    "Red",
    "France",
    "Bordeaux - Left Bank",
    "Pauillac",
    "Cabernet Sauvignon & Merlot",
)

wine2 = Wine(
    "Château Gloria",
    "Red",
    "France",
    "Bordeaux",
    "Paulliac",
    "Cab Sav",
)
wine3 = Wine(
    "Château Margaux",
    "White",
    "France",
    "Bordeaux",
    "St Julien",
    "Cab Sav",
)

wine4 = Wine(
    "Château Grand-Puy-Lacoste",
    "Orange",
    "France",
    "Bordeaux - Left Bank",
    "Pauillac",
    "Cabernet Sauvignon & Merlot",
)

winetable = WineTableDB()
winetable.insert(wine1)
winetable.insert(wine2)
winetable.insert(wine3)
winetable.insert(wine4)

query = QueryDB()

wines = query.fetch_by_colour("Red")
print("Fetch reds")
for wine in wines:
    print(wine)
print("*" * 15)

winetable.update_colour(1, "Blue")

wines = query.fetch_by_colour("Blue")
print("Colour change")
for wine in wines:
    print(wine)
print("*" * 15)

wines = query.fetch_by_country_and_name_and_reverse_colour_order("France")
print(
    "Name and reverse colour order"
)  # No need for sort index in transactions application?
for wine in wines:
    print(wine)
print("*" * 15)

print("Print all rows")
winetable.print_all_rows()
print("*" * 15)

winetable.delete(1)
# Best to use rowid if you are deleting or updating a record - this is its unique identifier - no need to wineID etc
print("Deleted record 1 - reprint all rows")
winetable.print_all_rows()
print("*" * 15)

wines = query.fetch_by_colour("White")
print("Fetch whites")
for wine in wines:
    print(wine)
print("*" * 15)


vintage1 = Vintage(
    "ID00001",
    2018,
    "BBR",
    "BBR",
    "In Bond",
    75,
    6,
    2,
    279.96,
    "ID00001.01",
    0,
    "Post-release",
    datetime(2023, 1, 4, 0, 0),
    datetime(2023, 1, 4, 0, 0),
)

review1 = Review(
    "ID00001",
    """The 2018 Grand-Puy-Lacoste is fabulous, just as it was from barrel. Strong \
Cabernet inflections soar out of the glass, giving the wine a compelling \
aromatic profile laced with the essence of graphite, dried herbs, menthol \
and dark fruit. One of the most classic (for lack of a better word) wines \
in the Left Bank in 2018, Grand-Puy-Lacoste is super-impressive right out \
of the gate. Grand-Puy-Lacoste is ultimately a wine of tremendous class \
that remains restrained and aristocratic in breeding. Don't miss it.
    """,
    "96",
    "Antonio Galloni",
    "2028 - 2048",
    "1st March 2021",
)


web1 = Websites(
    "ID00001",
    "cellartracker",
    "winesearcher",
)
