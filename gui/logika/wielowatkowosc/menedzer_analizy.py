from multiprocessing import Semaphore
from typing import Callable, Dict, List

from PyQt6.QtCore import QThread, QObject, pyqtSignal

from ...zawartosc.widgety.element_listy import ElementListy
from .analiza import Analiza


class MenedzerAnaliz(QObject):
    """
    Klasa służąca do tworzenia i zarządzania procesami wykonującymi analizy zdjęć
    """

    zakonczony = pyqtSignal()
    '''Sygnał informujący, że wszystkie zdjęcia zostały zaanalizowane'''

    def __init__(self, semafor: Semaphore, postep_analizy: pyqtSignal, utworz_pozycje: Callable[[str], ElementListy], watki: Dict[QThread, Analiza]) -> None:
        """
        :param semafor: Semafor ograniczający ilość wykonywanych procesów na raz
        :param postep_analizy: Sygnał do informowania o wykonaniu pojedynczej analizy zdjęcia
        :param utworz_pozycje: Funkcja tworząca nową pozycje na liście elementów na ekranie
        :param watki: Słownik do przechowywania referencji wykonywanych wątków i procesów analizy
        """

        super().__init__()
        self.semafor = semafor
        self.postep_analizy = postep_analizy
        self.watki = watki

        self.pozycje: Dict[str, ElementListy] = dict()
        self.utworz_pozycje = utworz_pozycje

    def ustaw_sciezki_do_analizy(self, sciezki: List[str]) -> None:
        """
        Ustawia listę ścieżek obrazów do poddania analizie
        :param sciezki: Lista scieżek obrazów do poddania analizie
        """
        for sciezka in sciezki:
            pozycja = self.utworz_pozycje(sciezka)
            self.pozycje[sciezka] = pozycja

    def analizuj(self) -> None:
        """
        Analizuje wszystkie obrazy spod ścieżek w self.pozycje
        """
        for sciezka in self.pozycje:
            self.semafor.acquire()

            watek = self.__utworz_watek()
            proces = self.__utworz_proces(sciezka, watek, gdy_zakonczony=self.pozycje[sciezka].ustaw_rodzaj)

            watek.started.connect(proces.rozpocznij)
            watek.start()

            self.__zapisz(watek, proces)

        while self.watki:
            pass  # Zaczekaj do zakończenia wszystkich wątków

        self.zakonczony.emit()

    def __utworz_watek(self) -> QThread:
        watek = QThread()
        watek.finished.connect(watek.deleteLater)
        watek.finished.connect(watek.exit)
        return watek

    def __utworz_proces(self, sciezka: str, watek_docelowy: QThread, gdy_zakonczony: Callable[[str], str]) -> Analiza:
        """
        Tworzy proces mający wykonać analize zdjęcia spod podanej ścieżki
        :param sciezka: Ścieżka zdjęcia, które ma zostac zanalizowane
        :param watek_docelowy: Watek, w którym ma działać proces
        :param gdy_zakonczony: Funkcja do wywołania po zakończeniu procesu
        """

        proces = Analiza(sciezka, self.semafor, self.watki, watek_docelowy, self.postep_analizy)
        proces.moveToThread(watek_docelowy)
        proces.odczytany_rodzaj.connect(gdy_zakonczony)
        proces.zakonczony.connect(proces.deleteLater)
        proces.zakonczony.connect(watek_docelowy.exit)
        return proces

    def __zapisz(self, watek: QThread, proces: Analiza) -> None:
        self.watki[watek] = proces