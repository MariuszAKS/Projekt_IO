from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QProgressBar

from ..motywy.menedzer_motywow import MenedzerMotywow
from ..designer.gui_designer import Ui_MainWindow
from ..okno import GlowneOkno
from ...logika.analizator_zdjec import AnalizatorZdjec
from ...logika.eksport.menedzer_eksportu import MenedzerEksportu
from .menedzer_listy import MenedzerListy
from .stylizator import Stylizator
from ...logika.wybor_plikow import wybierz_pliki


class Ui(Ui_MainWindow):
    def __init__(self, glowne_okno: GlowneOkno) -> None:
        super().__init__()
        self.__glowne_okno = glowne_okno
        self.setupUi(self.__glowne_okno)

        self.__analizator = AnalizatorZdjec()
        self.__mendzer_paska_ladowania = self.menedzer_paska_ladowania(self.pasek_ladowania,self.__analizator.postep_analizy)
        self.__stylizator = Stylizator(self.__glowne_okno)  # TODO: zmienić nazwę na bardziej znaczącą
        self.__menedzer_listy = MenedzerListy(lista_elementow=self.verticalLayout_2)
        self.__menedzer_motywow = MenedzerMotywow(self.__glowne_okno)
        self.__menedzer_eksportu = MenedzerEksportu(lista_elementow=self.verticalLayout_2)

        self.przycisk_dodaj.clicked.connect(self.pobierz_i_analizuj_zdjecia)
        self.przycisk_rodzaj.clicked.connect(self.__menedzer_listy.sortuj_po_rodzaju)
        self.przycisk_nazwa.clicked.connect(self.__menedzer_listy.sortuj_po_nazwie)
        self.przycisk_eksport.clicked.connect(self.__menedzer_eksportu.eksportuj)

        self.akcja_systemowy.triggered.connect(self.__menedzer_motywow.ustaw_systemowy)
        self.akcja_jasny.triggered.connect(self.__menedzer_motywow.ustaw_jasny)
        self.akcja_ciemny.triggered.connect(self.__menedzer_motywow.ustaw_ciemny)
        self.akcja_wysoki_kontrast.triggered.connect(self.__menedzer_motywow.ustaw_wysoki_kontrast)


    def pobierz_i_analizuj_zdjecia(self):
        sciezki = wybierz_pliki(self.__glowne_okno)

        self.__mendzer_paska_ladowania.uruchom_ladowanie(len(sciezki))
        self.__analizator.analizuj_zdjecia(sciezki, self.__menedzer_listy.utworz_pozycje)

    class menedzer_paska_ladowania():
        def __init__(self, pasek_ladowania: QProgressBar, sygnal_postepu: pyqtSignal) -> None:
            self.sygnal_postepu = sygnal_postepu
            self.pasek_ladowania = pasek_ladowania
            self.aktualny_stan = 0
            self.wielkosc_kroku = 100

            self.sygnal_postepu.connect(self.zwieksz_postep)

        def uruchom_ladowanie(self, liczba_elementow: int) -> None:
            self.aktualny_stan = 0
            self.pasek_ladowania.setValue(0)
            self.wielkosc_kroku = 100 / liczba_elementow

        def zwieksz_postep(self):
            self.aktualny_stan += self.wielkosc_kroku
            self.pasek_ladowania.setValue(int(self.aktualny_stan))



