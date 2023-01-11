import os

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog, QLabel, QMainWindow, QPushButton

from ..core.foldermanager import GUI_folder, invoice_folder, label_folder
from ..core.loaddata import wine1


class DisplayWine(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file and define the links
        with GUI_folder():
            uic.loadUi("wine.ui", self)

        self.winename = self.findChild(QLabel, "winenamelabel")
        self.vintage = self.findChild(QLabel, "vintagelabel")
        self.picture = self.findChild(QLabel, "picture")
        self.cellar = self.findChild(QLabel, "cellarlabel")
        self.merchant = self.findChild(QLabel, "merchantlabel")
        self.status = self.findChild(QLabel, "statuslabel")
        self.country = self.findChild(QLabel, "countrylabel")
        self.region = self.findChild(QLabel, "regionlabel")
        self.subregion = self.findChild(QLabel, "subregionlabel")
        self.grapetype = self.findChild(QLabel, "grapelabel")
        self.colour = self.findChild(QLabel, "colourlabel")
        self.wineID = self.findChild(QLabel, "wineIDlabel")
        self.casesize = self.findChild(QLabel, "casesizelabel")
        self.caseqty = self.findChild(QLabel, "caseqtylabel")
        self.bottleqty = self.findChild(QLabel, "bottleqtylabel")
        self.equiv75clbottleqty = self.findChild(QLabel, "equiv75clbottleqtylabel")
        self.equiv75clbottlecost = self.findChild(QLabel, "equiv75clbottlecostlabel")
        self.casecost = self.findChild(QLabel, "casecostlabel")
        self.bottlecost = self.findChild(QLabel, "bottlecostlabel")


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
            if wine.btlformatcl == 75:
                if vol == True:
                    return "75cl"
                else:
                    return "Bottles"
            elif wine.btlformatcl == 150:
                if vol == True:
                    return "150cl"
                else:
                    return "Magnums"
            elif wine.btlformatcl == 37.5:
                if vol == True:
                    return "37.5cl"
                else:
                    return "Half-bottles"
            elif wine.btlformatcl == 50:
                if vol == True:
                    return "50cl"
                else:
                    return "Jennies"

        # Set the wine to a Wine class object (temporarily set to wine1)
        wine = wine1
        # Set the GUI display
        self.winename.setText(wine.name)
        self.vintage.setText(str(wine.vintage))
        self.cellar.setText(wine.cellar)
        self.merchant.setText(wine.merchant)
        self.status.setText(wine.status)
        self.country.setText(wine.country)
        self.region.setText(wine.region)
        self.subregion.setText(wine.subregion)
        self.grapetype.setText(wine.grapetype)
        self.colour.setText(wine.colour)
        self.wineID.setText(wine.wineID)
        self.caseqty.setText(str(wine.caseqty))
        self.casesize.setText(str(wine.casesize) + " x " + formatsize(True))
        self.bottleqty.setText(str(wine.bottleqty) + "  (" + formatsize(False) + ")")
        self.equiv75clbottleqty.setText(str(wine.equiv75clbottleqty))
        self.equiv75clbottlecost.setText("£ " + str(wine.equiv75clbottlecost))
        self.casecost.setText("£ " + str(wine.casecost))
        self.bottlecost.setText("£ " + str(wine.bottlecost))

        with label_folder():
            filename = wine.wineID + " - Label.jpg"
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
