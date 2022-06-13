from __future__ import annotations
from ctypes import c_int16
from multiprocessing import Process, Semaphore, Value
from typing import Dict

from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QThread

from aplikacja_alpha.main import Rodzaj
from aplikacja_alpha.main import klasyfikuj as funkcja_analizujaca


class Analiza(QObject):
    odczytany_rodzaj = pyqtSignal(str)
    zakonczony = pyqtSignal()

    def __init__(self, sciezka_zdjecia: str, semafor: Semaphore, watki: Dict[QThread, Analiza], watek: QThread, postep_analizy: pyqtSignal) -> None:
        super().__init__()
        self.sciezka = sciezka_zdjecia
        self.rodzaj = Value(c_int16, -1)
        self.semafor = semafor
        self.watki = watki
        self.watek = watek
        self.postep_analizy = postep_analizy

    @pyqtSlot()
    def rozpocznij(self) -> None:
        self.watek.finished.connect(lambda: self.watki.pop(self.watek))
        proces = Process(target=_analizuj, args=(self.sciezka, self.rodzaj))
        proces.start()
        proces.join()

        rodzaj = ""
        try:
            rodzaj = str(Rodzaj(self.rodzaj.value))
        except ValueError:
            rodzaj = "Nastąpił błąd w wykonywaniu wątku"

        self.odczytany_rodzaj.emit(rodzaj)
        self.zakonczony.emit()
        self.postep_analizy.emit()
        self.semafor.release()
        self.watek.exit()


# Ze względu na zachowanie windowsa, bardzo ważne żeby ta funkcja była globalna (przynajmniej w zakresie tego pliku)
def _analizuj(sciezka: str, wartosc_zwrotna: Value) -> None:
    rodzaj = funkcja_analizujaca(sciezka)
    wartosc_zwrotna.value = rodzaj.value