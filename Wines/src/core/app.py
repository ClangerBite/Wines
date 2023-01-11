from PyQt6.QtWidgets import QApplication

from ..gui.wine import DisplayWine


def guirun():
    app = QApplication([])
    mainwin = DisplayWine()

    app.exec()
