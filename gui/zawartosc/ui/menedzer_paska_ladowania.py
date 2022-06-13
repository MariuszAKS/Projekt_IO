from PyQt6.QtWidgets import QProgressBar
from PyQt6.QtCore import pyqtSignal


class MenedzerPaskaLadowania:
    '''Klasa do kontrolowania zachowania paska ładowania'''

    def __init__(self, pasek_ladowania: QProgressBar, sygnal_postepu: pyqtSignal) -> None:
        """
        :param pasek_ladowania: Widżet paska ładowania
        :sygnal_postepu: Sygnał do emitowania informacji o postępie ładowania
        """

        self.sygnal_postepu = sygnal_postepu
        self.pasek_ladowania = pasek_ladowania
        self.aktualny_stan = 0
        self.wielkosc_kroku = 100

        self.sygnal_postepu.connect(self.__zwieksz_postep)

    def uruchom_ladowanie(self, liczba_elementow: int) -> None:
        """
        Ustawia ładowanie paska ładowania, dla określonej liczby elementów
        :param liczba_elementow: Liczba elementów, dla których wykonane będzie ładowanie
        """

        if liczba_elementow == 0: return

        self.aktualny_stan = 0
        self.pasek_ladowania.setValue(0)
        self.wielkosc_kroku = 100 / liczba_elementow

    def __zwieksz_postep(self) -> None:
        '''Zwiększa postęp ładowania paska ładowania o jeden krok'''

        self.aktualny_stan += self.wielkosc_kroku
        print(f"Postęp: {self.aktualny_stan}%")
        self.pasek_ladowania.setValue(int(self.aktualny_stan))