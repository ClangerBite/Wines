from datetime import datetime

from .datastructures import Review, Wine, Websites

wine1 = Wine(
    "ID00001",
    "Château Grand-Puy-Lacoste",
    "Red",
    "France",
    "Bordeaux - Left Bank",
    "Pauillac",
    "Cabernet Sauvignon & Merlot",
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
