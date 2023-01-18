from PyQt6.QtWidgets import QApplication

from ..gui.wine import DisplayWine
from .db_winetable import WineDBTable


def guirun():
    app = QApplication([])
    mainwin = DisplayWine()

    app.exec()
    wine = WineDBTable()
