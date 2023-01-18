from PyQt6.QtWidgets import QApplication

from ..gui.wine import DisplayWine
from .dbase import WineDB


def guirun():
    app = QApplication([])
    mainwin = DisplayWine()

    app.exec()
    wine = WineDB()
