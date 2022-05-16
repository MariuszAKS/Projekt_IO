import random as rand
from time import sleep
from logika.wybor_plikow import wybierz_pliki
from PyQt6.QtCore import QThread, QObject, pyqtSignal

lista = ["red", "blue", "green", "brown", "orange", "purple"]


def ustaw_dodawanie(ui):
    ui.watki = []
    ui.pushButton.clicked.connect(lambda: _analizuj_pliki(ui))

def _analizuj_pliki(ui):
    sciezki = wybierz_pliki(ui.widget_2)
    for sciezka in sciezki:
        ui.watki.append(_Watek(sciezka))

class _Watek():
    def __init__(self, sciezka: str) -> None:
        self.thread = QThread()
        self.worker = _Podproces(sciezka)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()


class _Podproces(QObject):
    finished = pyqtSignal()

    def __init__(self, sciezka: str) -> None:
        super().__init__()
        self.sciezka = sciezka
        self.lista = lista

    def run(self):
        rodzaj = _zwroc_rodzaj(self.sciezka)
        # zapisz gdzies rodzaj
        # verticalLayout_2.addWidget(ElementListy(self.scrollAreaWidgetContents))
        print(rodzaj)
        self.finished.emit()


def _zwroc_rodzaj(sciezka: str) -> str:
    sleep(rand.uniform(0.5, 2))
    rodzaj = rand.choice(lista)
    return rodzaj









