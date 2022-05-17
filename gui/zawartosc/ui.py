from typing import List

from PyQt6.QtWidgets import QVBoxLayout

from .designer.gui_designer import Ui_MainWindow
from .okno import GlowneOkno
from .widgety.element_listy import ElementListy
from ..logika.wybor_plikow import wybierz_pliki
from ..logika.imitacja_odczytywania_rodzaju import AnalizatorZdjec


class Ui(Ui_MainWindow):
    def __init__(self, glowne_okno: GlowneOkno) -> None:
        super().__init__()
        self.setupUi(glowne_okno)
        self.analizator = AnalizatorZdjec()
        self.menedzer_listy = MenedzerListy(lista_elementow=self.verticalLayout_2)
        self.przycisk_dodaj.clicked.connect(self.__analizuj_zdjecia)
        self.przycisk_rodzaj.clicked.connect(self.menedzer_listy.sortuj_po_rodzaju)
        self.przycisk_nazwa.clicked.connect(self.menedzer_listy.sortuj_po_nazwie)

    def __analizuj_zdjecia(self) -> None:
        sciezki = wybierz_pliki(self.obszar_przyciskow)
        self.menedzer_listy.usun_stare_pozycje()
        self.analizator.analizuj_zdjecia(sciezki, self.menedzer_listy.dodaj_pozycje)


class MenedzerListy:
    def __init__(self, lista_elementow: QVBoxLayout) -> None:
        self.__pozycje: List[ElementListy] = []
        self.__lista_elementow = lista_elementow
        self.__reverse = False

    def dodaj_pozycje(self, sciezka_zdjecia: str, rodzaj: str) -> None:
        nowy_element = ElementListy(sciezka_zdjecia, rodzaj)
        self.__lista_elementow.addWidget(nowy_element)
        self.__pozycje.append(nowy_element)

    def sortuj_po_rodzaju(self):
        self.__pozycje.sort(key=lambda x: x.rodzaj, reverse=self.__reverse)
        self.usun_stare_pozycje()
        self.__ustaw_nowe_pozycje()
        self.__reverse = not self.__reverse

    def sortuj_po_nazwie(self):
        self.__pozycje.sort(key=lambda x: x.sciezka, reverse=self.__reverse)
        self.usun_stare_pozycje()
        self.__ustaw_nowe_pozycje()
        self.__reverse = not self.__reverse

    def usun_stare_pozycje(self):
        for i in reversed(range(self.__lista_elementow.count())):
            self.__lista_elementow.itemAt(i).widget().setParent(None)

    def __ustaw_nowe_pozycje(self):
        for element in self.__pozycje:
            self.__lista_elementow.addWidget(element)


