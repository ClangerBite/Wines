import os

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QFileDialog, QLabel, QMainWindow, QPushButton

from ..core.directorymanager import directory, gui_folder, label_folder, invoice_folder
from ..core.loaddata import review1, wine1, vintage1


class DisplayWine(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file and define the links
        with directory(gui_folder):
            uic.loadUi("wine.ui", self)

        # Wine details in UI
        self.wineID = self.findChild(QLabel, "wineIDlabel")
        self.winename = self.findChild(QLabel, "winenamelabel")
        self.vintage = self.findChild(QLabel, "vintagelabel")
        self.picture = self.findChild(QLabel, "picture")
        self.country = self.findChild(QLabel, "countrylabel")
        self.region = self.findChild(QLabel, "regionlabel")
        self.subregion = self.findChild(QLabel, "subregionlabel")
        self.grapetype = self.findChild(QLabel, "grapelabel")
        self.colour = self.findChild(QLabel, "colourlabel")
        self.casesize = self.findChild(QLabel, "casesizelabel")
        self.caseqty = self.findChild(QLabel, "caseqtylabel")
        self.bottleqty = self.findChild(QLabel, "bottleqtylabel")
        self.equiv75clbottleqty = self.findChild(QLabel, "equiv75clbottleqtylabel")
        self.equiv75clbottlecost = self.findChild(QLabel, "equiv75clbottlecostlabel")
        self.casecost = self.findChild(QLabel, "casecostlabel")
        self.bottlecost = self.findChild(QLabel, "bottlecostlabel")
        self.total = self.findChild(QLabel, "totallabel")

        # Review details in UI
        self.review = self.findChild(QLabel, "reviewlabel")
        self.reviewer = self.findChild(QLabel, "reviewerlabel")
        self.score = self.findChild(QLabel, "scorelabel")
        self.drinkingwindow = self.findChild(QLabel, "drinkwindowlabel")
        self.reviewdate = self.findChild(QLabel, "reviewdatelabel")

        # Buttons in the UI
        self.loadbutton = self.findChild(QPushButton, "loadbutton")
        self.getfilebutton = self.findChild(QPushButton, "getfilebutton")
        self.savefilebutton = self.findChild(QPushButton, "savefilebutton")
        self.getfolderbutton = self.findChild(QPushButton, "getfolderbutton")

        # Define the activities
        self.loadbutton.clicked.connect(self.populate)
        self.getfilebutton.clicked.connect(self.get_filename)
        self.savefilebutton.clicked.connect(self.get_savefilename)
        self.getfolderbutton.clicked.connect(self.get_folder)

        self.show()

    def populate(self):
        def formatsize(vol: bool):
            if vintage.btlformatcl == 75:
                if vol == True:
                    return "75cl"
                else:
                    return "Bottles"
            elif vintage.btlformatcl == 150:
                if vol == True:
                    return "150cl"
                else:
                    return "Magnums"
            elif vintage.btlformatcl == 37.5:
                if vol == True:
                    return "37.5cl"
                else:
                    return "Half-bottles"
            elif vintage.btlformatcl == 50:
                if vol == True:
                    return "50cl"
                else:
                    return "Jennies"

        # Set the wine to a Wine class object (temporarily set to wine1)
        wine = wine1
        vintage = vintage1
        review = review1
        
        # Set the GUI display
        self.wineID.setText("TO BE DERIVED")
        self.winename.setText(wine.name)
        self.vintage.setText(str(vintage.vintage))
        self.country.setText(wine.country)
        self.region.setText(wine.region)
        self.subregion.setText(wine.subregion)
        self.grapetype.setText(wine.grapetype)
        self.colour.setText(wine.colour)
        self.caseqty.setText(str(vintage.caseqty))
        self.casesize.setText(str(vintage.casesize) + " x " + formatsize(True))
        self.bottleqty.setText(str(vintage.bottleqty) + "  (" + formatsize(False) + ")")
        self.equiv75clbottleqty.setText(str(vintage.equiv75clbottleqty))
        self.equiv75clbottlecost.setText("£ " + str(vintage.equiv75clbottlecost))
        self.casecost.setText("£ " + str(vintage.casecost))
        self.bottlecost.setText("£ " + str(vintage.bottlecost))
        self.total.setStyleSheet("background-color: lightyellow; color : #aa0000;")
        self.total.setText("£ " + str(vintage.casecost * vintage.caseqty))
        
        self.review.setText(review.text)
        self.reviewer.setStyleSheet("background-color: lightyellow")
        self.reviewer.setText(review.reviewer)
        self.score.setStyleSheet("background-color: lightyellow; color : #aa0000;")
        self.score.setText(review.score)
        self.drinkingwindow.setStyleSheet("background-color: lightyellow")
        self.drinkingwindow.setText(review.drinkingwindow)
        self.reviewdate.setText(review.reviewdate)        

        with directory(label_folder):
            filename = "ID00001" + " - Label.jpg" # TODO Get from DBASE
            self.pixmap = QPixmap(filename)
        self.picture.setPixmap(self.pixmap)

    def get_filename(self):
        # Gets a filename to open or use
        with label_folder():
            filename, _ = QFileDialog.getOpenFileName(
                parent=self,
                caption="Select a wine label file",
                directory=os.getcwd(),
                filter="All Files (*);; Picture Files (*.jpg *.png);; PDF Files (*.pdf)",
                initialFilter="Picture Files (*.jpg *.png)",
            )
        if filename:
            # DO SOMETHING
            self.winename.setText(filename)

    def get_savefilename(self):
        # Gets a filename to save to
        filename, _ = QFileDialog.getSaveFileName(
            parent=self,
            caption="Save file",
            directory=os.getcwd(),
            filter="All Files (*);; Picture Files (*.jpg *.png);; PDF Files (*.pdf)",
        )
        if filename:
            # DO SOMETHING
            self.winename.setText(filename)

    def get_folder(self):
        # Gets a folder name
        folder = QFileDialog.getExistingDirectory(
            parent=self, caption="Select a folder"
        )
        if folder:
            # DO SOMETHING
            self.winename.setText(folder)
