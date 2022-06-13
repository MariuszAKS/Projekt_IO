from __future__ import annotations

from PyQt6.QtGui import QIcon

from ..designer.gui_designer import Ui_MainWindow


_FOLDER_Z_IKONAMI = "gui/zasoby/ikony"


class LadowaczIkon:
    """
    Klasa do ładowania i zmiany ikon przycisków
    """

    PLUS = QIcon(f"{_FOLDER_Z_IKONAMI}/plus.svg")
    PLUS_KONTRAST = QIcon(f"{_FOLDER_Z_IKONAMI}/plus-kontrast.svg")

    DYSKIETKA = QIcon(f"{_FOLDER_Z_IKONAMI}/dyskietka.svg")
    DYSKIETKA_KONTRAST = QIcon(f"{_FOLDER_Z_IKONAMI}/dyskietka-kontrast.svg")

    KOSZ_JASNY = QIcon(f"{_FOLDER_Z_IKONAMI}/kosz-jasny.svg")
    KOSZ_CIEMNY = QIcon(f"{_FOLDER_Z_IKONAMI}/kosz-ciemny.svg")
    KOSZ_KONTRAST = QIcon(f"{_FOLDER_Z_IKONAMI}/kosz-kontrast.svg")

    LISTA_JASNY = QIcon(f"{_FOLDER_Z_IKONAMI}/lista-jasny.svg")
    LISTA_CIEMNY = QIcon(f"{_FOLDER_Z_IKONAMI}/lista-ciemny.svg")
    LISTA_KONTRAST = QIcon(f"{_FOLDER_Z_IKONAMI}/lista-kontrast.svg")


    def __init__(self, ui: Ui_MainWindow) -> None:
       self.ui = ui

    def zaladuj_jasne_ikony(self) -> None:
        self.__zaladuj_niezmienne_ikony()
        self.ui.przycisk_wyczysc.setIcon(self.KOSZ_JASNY)

    def zaladuj_ciemne_ikony(self)-> None:
        self.__zaladuj_niezmienne_ikony()
        self.ui.przycisk_wyczysc.setIcon(self.KOSZ_CIEMNY)

    def zaladuj_kontrastowe_ikony(self) -> None:
        self.ui.przycisk_dodaj.setIcon(self.PLUS_KONTRAST)
        self.ui.przycisk_eksport.setIcon(self.DYSKIETKA_KONTRAST)

    def __zaladuj_niezmienne_ikony(self) -> None:
        self.ui.przycisk_dodaj.setIcon(self.PLUS)
        self.ui.przycisk_eksport.setIcon(self.DYSKIETKA)