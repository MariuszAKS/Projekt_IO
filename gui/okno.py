import sys

from PyQt6.QtWidgets import *

from .ui.designer.gui import Ui_MainWindow
from .ui.glowne_okno import GlowneOkno
from .logika.imitacja_odczytywania_rodzaju import ustaw_dodawanie


class Aplikacja():
    def __init__(self) -> None:
        self.aplikacja = QApplication(sys.argv)
        self.okno = GlowneOkno()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.okno)
        ustaw_dodawanie(self.ui)

        sys.exit(self.aplikacja.exec())