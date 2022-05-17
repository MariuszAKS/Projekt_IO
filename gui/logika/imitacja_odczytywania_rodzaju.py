import random as rand
from time import sleep

from PyQt6.QtCore import QThread, QObject, pyqtSignal

from .wybor_plikow import wybierz_pliki
from ..ui.widgety.element_listy import dodaj_pozycje, usun_wszystkie_pozycje
from ..ui.designer.gui import Ui_MainWindow


lista = ["red", "blue", "green", "brown", "orange", "purple"]

def ustaw_dodawanie(ui: Ui_MainWindow) -> None:
    ui.watki = []
    ui.przycisk_dodaj.clicked.connect(lambda: _analizuj_pliki(ui))

def _analizuj_pliki(ui: Ui_MainWindow) -> None:
    sciezki = wybierz_pliki(ui.obszar_przyciskow)
    _usun_stare_pozycje(ui)

    for sciezka in sciezki:
        watek = _Watek(sciezka, ui)
        ui.watki.append(watek)


def _usun_stare_pozycje(ui: Ui_MainWindow) -> None:
    usun_wszystkie_pozycje(ui)
    ui.watki.clear()

class _Watek():
    def __init__(self, sciezka_zdjecia: str, ui: Ui_MainWindow) -> None:
        self.watek = QThread()
        self.proces = _Proces(sciezka_zdjecia)
        self.proces.moveToThread(self.watek)
        self.watek.started.connect(self.proces.run)
        self.proces.zakonczony.connect(lambda: dodaj_pozycje(ui, self.proces.sciezka, "zdjecie", self.proces.rodzaj))
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









