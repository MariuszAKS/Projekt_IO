from __future__ import annotations
import random as rand
from time import sleep
from typing import Callable, List


from PyQt6.QtCore import QThread, QObject, pyqtSignal

from ..zawartosc.designer.gui_designer import Ui_MainWindow


lista = ["red", "blue", "green", "brown", "orange", "purple"]


def _zwroc_rodzaj(sciezka_zdjecia: str) -> str:
    sleep(rand.uniform(0.5, 2))
    rodzaj = rand.choice(lista)
    print(rodzaj)
    return rodzaj


class AnalizatorZdjec:
    """Klasa sluzaca do przeprowadzania analizy zdjec"""

    def __init__(self) -> None:
        self.__watki = []

    def analizuj_zdjecia(self, sciezki: List[str], dodaj_pozycje: Callable[[str, str], None]) -> None:
        """
        Przeprowadza analize kazdego zdjecia z listy sciezki,
        nastepnie wywoluje funkcje dodaj_pozycje przy uzyciu uzyskanego wyniku

        Args:
            sciezki (List[str]): lista sciezek zdjec
            dodaj_pozycje (Callable[[str, str], None]): funkcja dodajaca pozycje do listy w ui
        """

        self.__watki.clear()

        for sciezka in sciezki:
            analiza = _Analiza(sciezka)
            watek = _Watek(
                proces_do_uruchomienia=analiza,
                gdy_zakonczony=dodaj_pozycje)

            self.__watki.append(watek)


class _Watek:
    def __init__(self, proces_do_uruchomienia: _Analiza, gdy_zakonczony: Callable[[str, str], None]) -> None:
        self.__watek = QThread()
        self.__proces = proces_do_uruchomienia
        self.__proces.moveToThread(self.__watek)
        self.__watek.started.connect(self.__proces.analizuj)
        self.__proces.zakonczony.connect(lambda: gdy_zakonczony(self.__proces.sciezka, self.__proces.rodzaj))
        self.__proces.zakonczony.connect(self.__watek.quit)
        self.__proces.zakonczony.connect(self.__proces.deleteLater)
        self.__watek.finished.connect(self.__watek.deleteLater)
        self.__watek.start()


class _Analiza(QObject):
    """Proces analizy pojedynczego zdjecia"""
    zakonczony = pyqtSignal()

    def __init__(self, sciezka_zdjecia: str) -> None:
        super().__init__()
        self.sciezka = sciezka_zdjecia
        self.rodzaj = None

    def analizuj(self):
        self.rodzaj = _zwroc_rodzaj(self.sciezka)
        self.zakonczony.emit()

