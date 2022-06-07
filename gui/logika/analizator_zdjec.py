from __future__ import annotations
from ctypes import c_int16
from multiprocessing import Process, Value
from typing import Callable, List, Dict

from PyQt6.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

from aplikacja_alpha.main import Rodzaj
from ..zawartosc.widgety.element_listy import ElementListy


class AnalizatorZdjec:
    '''Klasa sluzaca do przeprowadzania analizy zdjec'''

    funkcja_analizujaca: Callable[[str], str]
    '''Funkcja otrzymujaca sciezke zdjecia i zwracajaca rodzaj bakterii'''

    def __init__(self, funkcja_analizujaca: Callable[[str], str]) -> None:
        AnalizatorZdjec.funkcja_analizujaca = funkcja_analizujaca

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

        self.__usun_poprzednie_watki()

        for sciezka in sciezki:
            pozycja = utworz_pozycje(sciezka)

            watek = self.__utworz_watek()
            proces = self.__utworz_proces(sciezka, watek, gdy_zakonczony=pozycja.ustaw_rodzaj)

            watek.started.connect(proces.rozpocznij)

            self.__zapisz(watek, proces)
            watek.start()

    def __utworz_watek(self) -> QThread:
        watek = QThread()
        watek.finished.connect(watek.quit)
        watek.finished.connect(watek.deleteLater)
        watek.finished.connect(lambda: self.watki.pop(watek))
        return watek

    def __utworz_proces(self, sciezka: str, watek_docelowy: QThread, gdy_zakonczony: Callable[[str], str]) -> _Analiza:
        proces = _Analiza(sciezka)
        proces.moveToThread(watek_docelowy)
        proces.zakonczony.connect(gdy_zakonczony)
        proces.zakonczony.connect(proces.deleteLater)
        return proces

    def __zapisz(self, watek: QThread, proces: _Analiza) -> None:
        self.watki[watek] = proces

    def __usun_poprzednie_watki(self) -> None:
        for proces in self.watki:
            proces.exit()

        self.watki.clear()


class _Analiza(QObject):
    zakonczony = pyqtSignal(str)

    def __init__(self, sciezka) -> None:
        super().__init__()
        self.sciezka = sciezka
        self.rodzaj = Value(c_int16, -1)

    @pyqtSlot()
    def rozpocznij(self) -> None:
        proces = Process(target=self.__analizuj, args=(self.sciezka, self.rodzaj))
        proces.start()
        proces.join()
        self.zakonczony.emit(str(Rodzaj(self.rodzaj.value)))

    def __analizuj(self, sciezka: str, stary_rodzaj: Value) -> None:
        rodzaj = AnalizatorZdjec.funkcja_analizujaca(sciezka)
        stary_rodzaj.value = rodzaj.value
