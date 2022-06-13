import re

from PyQt6.QtGui import QShortcut, QKeySequence, QFont, QScrollEvent
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from ..okno import GlowneOkno

class MenedzerCzcionki:
    """
    Klasa ustawiająca skróty klawiszowe do zmiany rozmairu czcionki
    """

    def __init__(self, glowne_okno: GlowneOkno) -> None:

        self.__MAX_CZCIONKA = 70
        self.__MIN_CZCIONKA = 10
        self.__DOMYSLNA_CZCIONKA = 18

        self.__rozmiar_czcionki = self.__DOMYSLNA_CZCIONKA

        self.__glowne_okno = glowne_okno

        self.__skrot_powieksz = QShortcut(QKeySequence("Ctrl++"), glowne_okno)
        self.__skrot_powieksz.activated.connect(self.__powieksz_czcionke)

        self.__skrot_pomniejsz = QShortcut(QKeySequence("Ctrl+-"), glowne_okno)
        self.__skrot_pomniejsz.activated.connect(self.__zmniejsz_czcionke)

    def __powieksz_czcionke(self) -> None:
        '''Powiększa rozmiar czcionki o 1'''

        if self.__rozmiar_czcionki >= self.__MAX_CZCIONKA: return
        self.__rozmiar_czcionki += 1
        self.__ustaw_rozmiar_czcionki(self.__rozmiar_czcionki)

    def __zmniejsz_czcionke(self):
        '''Pomniejsza rozmiar czcionki o 1'''

        if self.__rozmiar_czcionki <= self.__MIN_CZCIONKA: return
        self.__rozmiar_czcionki -= 1
        self.__ustaw_rozmiar_czcionki(self.__rozmiar_czcionki)

    def __ustaw_rozmiar_czcionki(self, nowy_rozmiar: int) -> None:
        """
        Ustawia rozmiar czcionki
        :param nowy_rozmiar: Nowy rozmiar czcionki do ustawienia
        """

        stary_styl = self.__glowne_okno.styleSheet()

        stara_czcionka_widget = '''QWidget\{
    font-size: [0-9][0-9]'''

        nowa_czcionka_widget = '''QWidget{
    font-size: '''+str(nowy_rozmiar)

        nowy_styl = re.sub(stara_czcionka_widget, nowa_czcionka_widget, stary_styl)

        self.__glowne_okno.setStyleSheet(nowy_styl)