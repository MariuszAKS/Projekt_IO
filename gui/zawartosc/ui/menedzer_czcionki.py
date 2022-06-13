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
        self.__MIN_CZCIONKA = 1
        self.__DOMYSLNA_CZCIONKA = 16

        self.__rozmiar_czcionki = self.__DOMYSLNA_CZCIONKA

        self.__glowne_okno = glowne_okno

        self.__skrot_powieksz = QShortcut(QKeySequence("Ctrl++"), glowne_okno)
        self.__skrot_powieksz.activated.connect(self.__powieksz_czcionke)

        self.__skrot_pomniejsz = QShortcut(QKeySequence("Ctrl+-"), glowne_okno)
        self.__skrot_pomniejsz.activated.connect(self.__zmniejsz_czcionke)

        czcionka = glowne_okno.font()
        czcionka.setPointSize(self.__DOMYSLNA_CZCIONKA)
        # glowne_okno.setFont(czcionka)

        self.__ustaw_skrot_na_scroll()

    def __ustaw_skrot_na_scroll(self) -> None:
        '''Ustawia skrót to zmiany rozmiaru czcionki na scrollu'''

        def zmien_czcionke(event: QScrollEvent) -> None:
            '''Funkcja zmieniająca rozmiar czcionki przy scrollowaniu'''

            sila_ruchu_scrolla = event.angleDelta().y()
            czy_ctrl_wcisniety = QApplication.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier

            if czy_ctrl_wcisniety:
                if sila_ruchu_scrolla > 0:
                    self.__powieksz_czcionke()
                elif sila_ruchu_scrolla < 0:
                    self.__zmniejsz_czcionke()

            super(GlowneOkno, self.__glowne_okno).wheelEvent(event)

        self.__glowne_okno.wheelEvent = zmien_czcionke

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

        czcionka = QFont(self.__glowne_okno.font())
        czcionka.setPointSize(nowy_rozmiar)
        self.__glowne_okno.setFont(czcionka)