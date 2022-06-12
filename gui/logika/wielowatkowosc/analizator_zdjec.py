from __future__ import annotations
from typing import Callable, List, Optional
from multiprocessing import Semaphore

from PyQt6.QtCore import QThread, QObject, pyqtSignal

from ...zawartosc.widgety.element_listy import ElementListy
from .menedzer_analizy import MenedzerAnaliz


class AnalizatorZdjec(QObject):
    '''Klasa sluzaca do przeprowadzania analizy zdjec'''

    # MAKS_LICZBA_PROCESOW = cpu_count() - 1
    MAKS_LICZBA_PROCESOW = 2

    postep_analizy = pyqtSignal()

    def __init__(self, utworz_pozycje: Callable[[str], ElementListy]) -> None:
        super().__init__()
        '''Slownik sluzacy do przechowywania referencji do watkow i ich procesow'''
        self.semafor = Semaphore(self.MAKS_LICZBA_PROCESOW)
        self.aktualny_watek: Optional[QThread] = None
        self.watki = dict()
        self.menedzer_analiz: Optional[MenedzerAnaliz]
        self.utworz_pozycje = utworz_pozycje


    def analizuj_zdjecia(self, sciezki: List[str]) -> None:
        """
        Przeprowadza analize kazdego zdjecia z listy sciezki,
        nastepnie wywoluje funkcje dodaj_pozycje przy uzyciu uzyskanego wyniku

        Args:
            sciezki (List[str]): lista sciezek zdjec
            dodaj_pozycje (Callable[[str, str], None]): funkcja dodajaca pozycje do listy w ui
        """

        self.menedzer_analiz = MenedzerAnaliz(self.semafor, self.postep_analizy, self.utworz_pozycje, self.watki)
        self.menedzer_analiz.ustaw_sciezki_do_analizy(sciezki)

        nowy_watek = QThread()
        nowy_watek.finished.connect(nowy_watek.exit)

        self.menedzer_analiz.moveToThread(nowy_watek)
        self.menedzer_analiz.zakonczony.connect(self.menedzer_analiz.deleteLater)
        self.menedzer_analiz.zakonczony.connect(nowy_watek.exit)

        nowy_watek.started.connect(self.menedzer_analiz.analizuj)


        if self.aktualny_watek is not None:
            self.aktualny_watek.exit()

        self.aktualny_watek = nowy_watek
        nowy_watek.start()