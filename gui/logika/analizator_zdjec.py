from __future__ import annotations
from typing import Callable, List

from PyQt6.QtCore import QThread, QObject, pyqtSignal

from ..zawartosc.widgety.element_listy import ElementListy


class AnalizatorZdjec:
    """Klasa sluzaca do przeprowadzania analizy zdjec"""

    def __init__(self, funkcja_analizujaca: Callable[[str], str]) -> None:
        self.__watki: List[_Watek] = []
        AnalizatorZdjec.funkcja_analizujaca = funkcja_analizujaca

    def analizuj_zdjecia(self, sciezki: List[str], dodaj_pozycje: Callable[[str], ElementListy]) -> None:
        """
        Przeprowadza analize kazdego zdjecia z listy sciezki,
        nastepnie wywoluje funkcje dodaj_pozycje przy uzyciu uzyskanego wyniku

        Args:
            sciezki (List[str]): lista sciezek zdjec
            dodaj_pozycje (Callable[[str, str], None]): funkcja dodajaca pozycje do listy w ui
        """

        self.__watki.clear()

        for sciezka in sciezki:
            proces_analizy = _Analiza(sciezka)
            element_listy = dodaj_pozycje(sciezka)

            watek = _Watek(
                proces_do_uruchomienia=proces_analizy,
                gdy_zakonczony=element_listy.ustaw_rodzaj)

            self.__watki.append(watek)

        for watek in self.__watki:
            watek.rozpocznij()


class _Watek:
    def __init__(self, proces_do_uruchomienia: _Analiza, gdy_zakonczony: Callable[[str], None]) -> None:
        self.__watek = QThread()
        self.__proces = proces_do_uruchomienia
        self.__proces.moveToThread(self.__watek)
        self.__watek.started.connect(self.__proces.analizuj)
        self.__proces.zakonczony.connect(lambda: gdy_zakonczony(self.__proces.rodzaj))
        self.__proces.zakonczony.connect(self.__watek.quit)
        self.__proces.zakonczony.connect(self.__proces.deleteLater)
        self.__watek.finished.connect(self.__watek.deleteLater)

    def rozpocznij(self):
        self.__watek.start()


class _Analiza(QObject):
    """Proces analizy pojedynczego zdjecia"""
    zakonczony = pyqtSignal()

    def __init__(self, sciezka_zdjecia: str) -> None:
        super().__init__()
        self.sciezka = sciezka_zdjecia
        self.rodzaj = None

    def analizuj(self):
        self.rodzaj = AnalizatorZdjec.funkcja_analizujaca(self.sciezka)
        self.zakonczony.emit()

