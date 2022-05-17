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
    return rodzaj

class AnalizatorZdjec():
    '''Klasa sluzaca do przeprowadzania analizy zdjec'''

    def __init__(self) -> None:
        self.watki = []

    def analizuj_zdjecia(self, sciezki: List[str], dodaj_pozycje: Callable[[str, str], None]) -> None:
        """
        Przeprowadza analize kazdego zdjecia z listy sciezki,
        nastepnie wywoluje funkcje dodaj_pozycje przy uzyciu uzyskanego wyniku

        Args:
            sciezki (List[str]): lista sciezek zdjec
            dodaj_pozycje (Callable[[str, str], None]): funkcja dodajaca pozycje do listy w ui
        """

        self.watki.clear()

        for sciezka in sciezki:

            analiza = _Analiza(sciezka)
            watek = _Watek(
                proces_do_uruchomienia=analiza,
                gdy_zakonczony=dodaj_pozycje)

            self.watki.append(watek)


class _Watek():
    def __init__(self, proces_do_uruchomienia: _Analiza, gdy_zakonczony: Callable[[str, str], None]) -> None:
        self.watek = QThread()
        self.proces = proces_do_uruchomienia
        self.proces.moveToThread(self.watek)
        self.watek.started.connect(self.proces.analizuj)
        self.proces.zakonczony.connect(lambda: gdy_zakonczony(self.proces.sciezka, self.proces.rodzaj))
        self.proces.zakonczony.connect(self.watek.quit)
        self.proces.zakonczony.connect(self.proces.deleteLater)
        self.watek.finished.connect(self.watek.deleteLater)
        self.watek.start()


class _Analiza(QObject):
    """Proces analizy pojedynczego zdjecia"""
    zakonczony = pyqtSignal()

    def __init__(self, sciezka_zdjecia: str) -> None:
        super().__init__()
        self.sciezka = sciezka_zdjecia
        self.lista = lista
        self.rodzaj = None

    def analizuj(self):
        self.rodzaj = _zwroc_rodzaj(self.sciezka)
        print(self.rodzaj)
        self.zakonczony.emit()

