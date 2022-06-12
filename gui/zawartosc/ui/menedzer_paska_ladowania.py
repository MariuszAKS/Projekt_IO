from PyQt6.QtWidgets import QProgressBar
from PyQt6.QtCore import pyqtSignal


class MenedzerPaskaLadowania:
        def __init__(self, pasek_ladowania: QProgressBar, sygnal_postepu: pyqtSignal) -> None:
            self.sygnal_postepu = sygnal_postepu
            self.pasek_ladowania = pasek_ladowania
            self.aktualny_stan = 0
            self.wielkosc_kroku = 100

            self.sygnal_postepu.connect(self.zwieksz_postep)

        def uruchom_ladowanie(self, liczba_elementow: int) -> None:
            if liczba_elementow == 0: return

            self.aktualny_stan = 0
            self.pasek_ladowania.setValue(0)
            self.wielkosc_kroku = 100 / liczba_elementow

        def zwieksz_postep(self):
            self.aktualny_stan += self.wielkosc_kroku
            print(f"Postęp: {self.aktualny_stan}%")
            self.pasek_ladowania.setValue(int(self.aktualny_stan))