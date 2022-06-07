from __future__ import annotations
from ctypes import c_int16
from multiprocessing import Process, Value
from typing import Callable, List, Dict

from PyQt6.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QProgressBar

from aplikacja_alpha.main import Rodzaj
from ..zawartosc.widgety.element_listy import ElementListy
from aplikacja_alpha.main import klasyfikuj as funkcja_analizujaca


class AnalizatorZdjec(QObject):
    '''Klasa sluzaca do przeprowadzania analizy zdjec'''

    postep_analizy = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.watki: Dict[QThread, _Analiza] = dict()
        '''Slownik sluzacy do przechowywania referencji do watkow i ich procesow'''

    def analizuj_zdjecia(self, sciezki: List[str], utworz_pozycje: Callable[[str], ElementListy]) -> None:
        """
        Przeprowadza analize kazdego zdjecia z listy sciezki,
        nastepnie wywoluje funkcje dodaj_pozycje przy uzyciu uzyskanego wyniku

        Args:
            sciezki (List[str]): lista sciezek zdjec
            dodaj_pozycje (Callable[[str, str], None]): funkcja dodajaca pozycje do listy w ui
        """

        for sciezka in sciezki:
            pozycja = utworz_pozycje(sciezka)

            watek = self.__utworz_watek()
            proces = self.__utworz_proces(sciezka, watek, gdy_zakonczony=pozycja.ustaw_rodzaj)

            watek.started.connect(proces.rozpocznij)

            self.__zapisz(watek, proces)
            watek.start()

    def __utworz_watek(self) -> QThread:
        watek = QThread()
        watek.finished.connect(watek.deleteLater)
        watek.finished.connect(watek.exit)
        watek.finished.connect(lambda: self.watki.pop(watek))
        return watek

    def __utworz_proces(self, sciezka: str, watek_docelowy: QThread, gdy_zakonczony: Callable[[str], str]) -> _Analiza:
        proces = _Analiza(sciezka)
        proces.moveToThread(watek_docelowy)
        proces.zakonczony.connect(gdy_zakonczony)
        proces.zakonczony.connect(self.postep_analizy.emit)
        proces.zakonczony.connect(proces.deleteLater)
        proces.zakonczony.connect(watek_docelowy.exit)
        return proces

    def __zapisz(self, watek: QThread, proces: _Analiza) -> None:
        self.watki[watek] = proces



class _Analiza(QObject):
    zakonczony = pyqtSignal(str)

    def __init__(self, sciezka) -> None:
        super().__init__()
        self.sciezka = sciezka
        self.rodzaj = Value(c_int16, -1)

    @pyqtSlot()
    def rozpocznij(self) -> None:
        proces = Process(target=_analizuj, args=(self.sciezka, self.rodzaj))
        proces.start()
        proces.join()

        rodzaj = ""
        try:
            rodzaj = str(Rodzaj(self.rodzaj.value))
        except ValueError:
            rodzaj = "Nastąpił błąd w wykonywaniu wątku"

        self.zakonczony.emit(rodzaj)

# Ze względu na zachowanie windowsa, bardzo ważne żeby ta funkcja była globalna (przynajmniej w zakresie tego pliku)
def _analizuj(sciezka: str, wartosc_zwrotna: Value) -> None:
    rodzaj = funkcja_analizujaca(sciezka)
    wartosc_zwrotna.value = rodzaj.value
