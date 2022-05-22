import sys
from typing import Callable

from PyQt6.QtWidgets import *

from .zawartosc.ui.ui import Ui
from .zawartosc.okno import GlowneOkno


class Aplikacja:
    def __init__(self, funkcja_analizujaca: Callable[[str],str]) -> None:
        self.__aplikacja = QApplication(sys.argv)
        self.__okno = GlowneOkno()
        self.__ui = Ui(self.__okno, funkcja_analizujaca)

        sys.exit(self.__aplikacja.exec())
