from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Wine:    
    #wineID: str
    name: str
    colour: str
    country: str        # don't need this as can include in separate look-up table based on subregion
    region: str         # don't need this as can include in separate look-up table based on subregion
    subregion: str
    grapetype: str

@dataclass(order=True)
class Vintage:
    bottleqty: int = field(init=False, repr=False)
    bottlecost: float = field(init=False, repr=False)
    equiv75clbottleqty: float = field(init=False, repr=False)
    equiv75clbottlecost: float = field(init=False, repr=False)   
    sort_index: str = field(init=False, repr=False)
    
    wineID: str
    vintage: int
    
    # belong in a Case structure - link with vintageID
    merchant: str
    cellar: str
    status: str    
    btlformatcl: float
    casesize: int
    caseqty: int
    casecost: float
    caseID: str
    casesplit: int
    source: str
    datebought: datetime
    datedelivered: datetime
    

    def __post_init__(self) -> None:   
        self.bottleqty = self.casesize * self.caseqty
        self.bottlecost: float = self.casecost / self.casesize
        self.equiv75clbottleqty: float = self.bottleqty * self.btlformatcl / 75
        self.equiv75clbottlecost: float = self.casecost / self.equiv75clbottleqty   
        self.sort_index: str = "001|001|001|001|001|"   # base this on separate look-up table with numbers based on country/region/subregion/vintage/name/bottleformat - or (better) can do this by a GUI-input sort order



@dataclass
class Review:
    wineID: str
    text: str
    score: str
    reviewer: str
    drinkingwindow: str
    reviewdate: str

@dataclass
class Websites:
    wineID: str
    cellartracker: str
    winesearcher: str