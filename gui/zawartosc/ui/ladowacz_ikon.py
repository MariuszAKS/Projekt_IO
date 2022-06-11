from __future__ import annotations

from PyQt6.QtGui import QIcon

from ..designer.gui_designer import Ui_MainWindow

_FOLDER_Z_IKONAMI = "gui/zasoby/ikony"

class LadowaczIkon:

    PLUS = QIcon(f"{_FOLDER_Z_IKONAMI}/plus.svg")
    DYSKIETKA = QIcon(f"{_FOLDER_Z_IKONAMI}/dyskietka.svg")
    KOSZ = QIcon(f"{_FOLDER_Z_IKONAMI}/kosz.svg")
    LISTA = QIcon(f"{_FOLDER_Z_IKONAMI}/lista.svg")

    def __init__(self, ui: Ui_MainWindow) -> None:
       self.ui = ui

    def zaladuj_ikony(self):
        self.ui.przycisk_dodaj.setIcon(self.PLUS)
        self.ui.przycisk_eksport.setIcon(self.DYSKIETKA)
        self.ui.przycisk_wyczysc.setIcon(self.KOSZ)
        self.ui.przycisk_zmien_uklad.setIcon(self.LISTA)