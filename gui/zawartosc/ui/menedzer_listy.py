from typing import List

from PyQt6.QtWidgets import QVBoxLayout

from ..widgety.element_listy import ElementListy


class MenedzerListy:
    def __init__(self, lista_elementow: QVBoxLayout) -> None:
        self.pozycje: List[ElementListy] = []
        self.__lista_elementow = lista_elementow
        self.__reverse = False

    def sortuj_po_rodzaju(self) -> None:
        self.pozycje.sort(key=lambda x: x.rodzaj, reverse=self.__reverse)
        self.usun_stare_pozycje()
        self.__ustaw_nowe_pozycje()
        self.__reverse = not self.__reverse

    def sortuj_po_nazwie(self) -> None:
        self.pozycje.sort(key=lambda x: x.nazwa, reverse=self.__reverse)
        self.usun_stare_pozycje()
        self.__ustaw_nowe_pozycje()
        self.__reverse = not self.__reverse

    def usun_stare_pozycje(self) -> None:
        for i in reversed(range(self.__lista_elementow.count())):
            self.__lista_elementow.itemAt(i).widget().setParent(None)

    def utworz_pozycje(self, sciezka_zdjecia: str) -> ElementListy:
        nowy_element = ElementListy(sciezka_zdjecia)
        self.__lista_elementow.addWidget(nowy_element)
        self.pozycje.append(nowy_element)
        return nowy_element

    def __ustaw_nowe_pozycje(self) -> None:
        for element in self.pozycje:
            self.__lista_elementow.addWidget(element)