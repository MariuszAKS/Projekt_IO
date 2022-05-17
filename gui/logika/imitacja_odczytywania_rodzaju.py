import random as rand
from time import sleep
from typing import Callable

from PyQt6.QtCore import QThread, QObject, pyqtSignal

from ..zawartosc.designer.gui_designer import Ui_MainWindow


lista = ["red", "blue", "green", "brown", "orange", "purple"]

class AnalizatorZdjec():
    def __init__(self) -> None:
        self.watki = []

    def ustaw_dodawanie(self, ui: Ui_MainWindow) -> None:
        ui.watki = []
        ui.przycisk_dodaj.clicked.connect(lambda: self.analizuj_pliki(ui))

    def analizuj_zdjecia(self, sciezki: list, dodaj_pozycje: Callable[[str, str], None]) -> None:
        self.watki.clear()
        for sciezka in sciezki:
            watek = _Watek(sciezka, dodaj_pozycje)
            self.watki.append(watek)


class _Watek():
    def __init__(self, sciezka_zdjecia: str, dodaj_pozycje: Callable[[str, str], None]) -> None:
        self.watek = QThread()
        self.proces = _Proces(sciezka_zdjecia)
        self.proces.moveToThread(self.watek)
        self.watek.started.connect(self.proces.run)
        self.proces.zakonczony.connect(lambda: dodaj_pozycje(self.proces.sciezka, self.proces.rodzaj))
        self.proces.zakonczony.connect(self.watek.quit)
        self.proces.zakonczony.connect(self.proces.deleteLater)
        self.watek.finished.connect(self.watek.deleteLater)
        self.watek.start()


class _Proces(QObject):
    zakonczony = pyqtSignal()

    def __init__(self, sciezka_zdjecia: str) -> None:
        super().__init__()
        self.sciezka = sciezka_zdjecia
        self.lista = lista
        self.rodzaj = None

    def run(self):
        self.rodzaj = _zwroc_rodzaj(self.sciezka)
        print(self.rodzaj)
        self.zakonczony.emit()


def _zwroc_rodzaj(sciezka_zdjecia: str) -> str:
    sleep(rand.uniform(0.5, 2))
    rodzaj = rand.choice(lista)
    return rodzaj









