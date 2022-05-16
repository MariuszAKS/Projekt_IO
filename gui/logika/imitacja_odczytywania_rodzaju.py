import random as rand
from time import sleep
from logika.wybor_plikow import wybierz_pliki
from PyQt6.QtCore import QThread, QObject, pyqtSignal
from ui.element_listy import dodaj_pozycje
from ui.gui import Ui_MainWindow

lista = ["red", "blue", "green", "brown", "orange", "purple"]


def ustaw_dodawanie(ui: Ui_MainWindow):
    ui.watki = []
    ui.pushButton.clicked.connect(lambda: _analizuj_pliki(ui))

def _analizuj_pliki(ui: Ui_MainWindow):
    sciezki = wybierz_pliki(ui.widget_2)
    for sciezka in sciezki:
        watek = _Watek(sciezka, ui)
        ui.watki.append(watek)

class _Watek():
    def __init__(self, sciezka: str, ui: Ui_MainWindow) -> None:
        self.watek = QThread()
        self.proces = _Proces(sciezka)
        self.proces.moveToThread(self.watek)
        self.watek.started.connect(self.proces.run)
        self.proces.zakonczony.connect(lambda: dodaj_pozycje(ui, self))
        self.proces.zakonczony.connect(self.watek.quit)
        self.proces.zakonczony.connect(self.proces.deleteLater)
        self.watek.finished.connect(self.watek.deleteLater)
        self.watek.start()


class _Proces(QObject):
    zakonczony = pyqtSignal()

    def __init__(self, sciezka: str) -> None:
        super().__init__()
        self.sciezka = sciezka
        self.lista = lista
        self.rodzaj = None

    def run(self):
        self.rodzaj = _zwroc_rodzaj(self.sciezka)
        print(self.rodzaj)
        self.zakonczony.emit()


def _zwroc_rodzaj(sciezka: str) -> str:
    sleep(rand.uniform(0.5, 2))
    rodzaj = rand.choice(lista)
    return rodzaj









