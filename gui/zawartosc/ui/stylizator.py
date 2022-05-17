from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from ..okno import GlowneOkno


class Stylizator:
    def __init__(self, glowne_okno: GlowneOkno) -> None:

        self.__MAX_CZCIONKA = 70
        self.__MIN_CZCIONKA = 1

        self.__glowne_okno = glowne_okno
        self.__rozmiar_czcionki = 12

        self.__skrot_powieksz = QShortcut(QKeySequence("Ctrl++"), glowne_okno)
        self.__skrot_powieksz.activated.connect(self.__powieksz_czcionke)

        self.__skrot_pomniejsz = QShortcut(QKeySequence("Ctrl+-"), glowne_okno)
        self.__skrot_pomniejsz.activated.connect(self.__zmniejsz_czcionke)

        self.__ustaw_skrot_na_scroll()

    def __ustaw_skrot_na_scroll(self):
        def zmien_czcionke(event):
            sila_ruchu_scrolla = event.angleDelta().y()
            czy_ctrl_wcisniety = QApplication.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier

            if czy_ctrl_wcisniety:
                if sila_ruchu_scrolla > 0:
                    self.__powieksz_czcionke()
                elif sila_ruchu_scrolla < 0:
                    self.__zmniejsz_czcionke()

            super(GlowneOkno, self.__glowne_okno).wheelEvent(event)

        self.__glowne_okno.wheelEvent = zmien_czcionke

    def __powieksz_czcionke(self):
        if self.__rozmiar_czcionki >= self.__MAX_CZCIONKA: return
        self.__rozmiar_czcionki += 1
        self.__ustaw_rozmiar_czcionki(self.__rozmiar_czcionki)

    def __zmniejsz_czcionke(self):
        if self.__rozmiar_czcionki <= self.__MIN_CZCIONKA: return
        self.__rozmiar_czcionki -= 1
        self.__ustaw_rozmiar_czcionki(self.__rozmiar_czcionki)

    def __ustaw_rozmiar_czcionki(self, rozmiar: int):
        self.__glowne_okno.setStyleSheet("""
            QWidget{
                font-size: """ + str(rozmiar) + """px;
            }
        """)
