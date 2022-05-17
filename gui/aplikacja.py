import sys

from PyQt6.QtWidgets import *

from .zawartosc.ui.ui import Ui
from .zawartosc.okno import GlowneOkno


class Aplikacja():
    def __init__(self) -> None:
        self.__aplikacja = QApplication(sys.argv)
        self.__okno = GlowneOkno()
        self.__ui = Ui(self.__okno)

        sys.exit(self.__aplikacja.exec())
