from typing import Callable, Dict, List

from PyQt6.QtCore import QThread, QObject, pyqtSignal

from gui.zawartosc.widgety.element_listy import ElementListy

from .analiza import Analiza


class MenedzerAnaliz(QObject):
    zakonczony = pyqtSignal()

    def __init__(self, semafor, postep_analizy, utworz_pozycje, watki: Dict[QThread, Analiza]) -> None:
        super().__init__()
        self.semafor = semafor
        self.postep_analizy = postep_analizy
        self.watki = watki

        self.pozycje: Dict[str, ElementListy] = dict()
        self.utworz_pozycje = utworz_pozycje

    def ustaw_sciezki_do_analizy(self, sciezki: List[str]) -> None:
        for sciezka in sciezki:
            pozycja = self.utworz_pozycje(sciezka)
            self.pozycje[sciezka] = pozycja

    def analizuj(self) -> None:
        for sciezka in self.pozycje:
            self.semafor.acquire()
            print(f"ILOSC WATKOW: {len(self.watki)}")

            watek = self.__utworz_watek()
            proces = self.__utworz_proces(sciezka, watek, gdy_zakonczony=self.pozycje[sciezka].ustaw_rodzaj)

            watek.started.connect(proces.rozpocznij)

            self.__zapisz(watek, proces)
            watek.start()

        while self.watki:
            pass

        self.zakonczony.emit()

    def __utworz_watek(self) -> QThread:
        watek = QThread()
        watek.finished.connect(watek.deleteLater)
        watek.finished.connect(watek.exit)
        return watek

    def __utworz_proces(self, sciezka: str, watek_docelowy: QThread, gdy_zakonczony: Callable[[str], str]) -> Analiza:
        proces = Analiza(sciezka, self.semafor, self.watki, watek_docelowy, self.postep_analizy)
        proces.moveToThread(watek_docelowy)
        proces.odczytany_rodzaj.connect(gdy_zakonczony)
        proces.zakonczony.connect(proces.deleteLater)
        proces.zakonczony.connect(watek_docelowy.exit)
        return proces

    def __zapisz(self, watek: QThread, proces: Analiza) -> None:
        self.watki[watek] = proces