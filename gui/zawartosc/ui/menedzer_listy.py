from typing import List

from PyQt6.QtWidgets import QVBoxLayout

from ..widgety.element_listy import ElementListy


class MenedzerListy:
    """
    Klasa do zarządzania główną listą ze zdjęciami i rodzajami w GUI
    """

    def __init__(self, lista_elementow: QVBoxLayout) -> None:
        """
        :param lista_elementow: Widżet przechowujący wszystkie pozycje listy
        """

        self.pozycje: List[ElementListy] = []
        '''Dodatkowa lista elementów służaca do ich łatwego i szybkiego sortowania'''

        self.__lista_elementow = lista_elementow
        self.__reverse = False

    def sortuj_po_rodzaju(self) -> None:
        '''Sortuje elementy na liście po rodzaju. Jeśli elementy były już wcześniej sortowane to zostaną posortowane na odwrót'''

        self.pozycje.sort(key=lambda x: x.rodzaj, reverse=self.__reverse)
        self.__usun_stare_pozycje()
        self.__ustaw_nowe_pozycje()
        self.__reverse = not self.__reverse

    def sortuj_po_nazwie(self) -> None:
        '''Sortuje elementy na liście po nazwie pliku. Jeśli elementy były już wcześniej sortowane to zostaną posortowane na odwrót'''

        self.pozycje.sort(key=lambda x: x.nazwa, reverse=self.__reverse)
        self.__usun_stare_pozycje()
        self.__ustaw_nowe_pozycje()
        self.__reverse = not self.__reverse

    def utworz_pozycje(self, sciezka_zdjecia: str) -> ElementListy:
        """
        Dodaje nową pozycję na listę
        :param sciezka_zdjecia: Scieżka zdjęcia do dodania na listę
        :return: Nowo utworzony element, zawierający podane zdjęcie
        """

        nowy_element = ElementListy(sciezka_zdjecia)
        self.__lista_elementow.addWidget(nowy_element)
        self.pozycje.append(nowy_element)
        return nowy_element

    def wyczysc_liste(self) -> None:
        '''Usuwa na stałe wszystkie elementy z listy'''

        self.__usun_stare_pozycje()
        self.pozycje.clear()

    def __usun_stare_pozycje(self) -> None:
        '''Usuwa wszyskie elementy z widżetu listy, ale zachowuje te w self.pozycje, aby można było je wyświetlić ponownie'''

        for i in reversed(range(self.__lista_elementow.count())):
            self.__lista_elementow.itemAt(i).widget().setParent(None)


    def __ustaw_nowe_pozycje(self) -> None:
        '''Dodaje na listę elementy z self.pozycje w dokładnej ich kolejności'''

        for element in self.pozycje:
            self.__lista_elementow.addWidget(element)