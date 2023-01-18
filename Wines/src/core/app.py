from PyQt6.QtWidgets import QApplication

from ..gui.wine import DisplayWine


def run_gui():
    app = QApplication([])
    mainwin = DisplayWine()

    app.exec()
