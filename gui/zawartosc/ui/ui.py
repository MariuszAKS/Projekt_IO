from .ladowacz_ikon import LadowaczIkon
from .menedzer_listy import MenedzerListy
from .menedzer_czcionki import MenedzerCzcionki
from .menedzer_paska_ladowania import MenedzerPaskaLadowania
from ..motywy.menedzer_motywow import MenedzerMotywow
from ..designer.gui_designer import Ui_MainWindow
from ..okno import GlowneOkno
from ...logika.analizator_zdjec import AnalizatorZdjec
from ...logika.eksport.menedzer_eksportu import MenedzerEksportu
from ...logika.wybor_plikow import wybierz_pliki

from PyQt6.QtCore import QThread


class Ui(Ui_MainWindow):
    def __init__(self, glowne_okno: GlowneOkno) -> None:
        super().__init__()
        self.__glowne_okno = glowne_okno
        self.setupUi(self.__glowne_okno)

        self.__analizator = AnalizatorZdjec()
        self.__ladowacz_ikon = LadowaczIkon(self)
        self.__mendzer_paska_ladowania = MenedzerPaskaLadowania(self.pasek_ladowania, self.__analizator.postep_analizy)
        self.__menedzer_fontu = MenedzerCzcionki(self.__glowne_okno)
        self.__menedzer_listy = MenedzerListy(lista_elementow=self.verticalLayout_2)
        self.__menedzer_motywow = MenedzerMotywow(self.__glowne_okno)
        self.__menedzer_eksportu = MenedzerEksportu(lista_elementow=self.__menedzer_listy.pozycje, rodzic=self.__glowne_okno)

        self.__menedzer_motywow.ustaw_ciemny()
        self.__ladowacz_ikon.zaladuj_jasne_ikony()
        self.__dodaj_akcje_przyciskow()
        self.__dodaj_akcje_menu_motywow()

    def __pobierz_i_analizuj_zdjecia(self):
        sciezki = wybierz_pliki(self.__glowne_okno)

        self.__mendzer_paska_ladowania.uruchom_ladowanie(len(sciezki))
        self.__analizator.analizuj_zdjecia(sciezki, self.__menedzer_listy.utworz_pozycje)

    def __dodaj_akcje_przyciskow(self):
        self.przycisk_dodaj.clicked.connect(self.__pobierz_i_analizuj_zdjecia)
        self.przycisk_rodzaj.clicked.connect(self.__menedzer_listy.sortuj_po_rodzaju)
        self.przycisk_nazwa.clicked.connect(self.__menedzer_listy.sortuj_po_nazwie)
        self.przycisk_eksport.clicked.connect(self.__menedzer_eksportu.eksportuj)
        self.przycisk_wyczysc.clicked.connect(self.__menedzer_listy.usun_stare_pozycje)

    def __dodaj_akcje_menu_motywow(self):
        self.akcja_systemowy.triggered.connect(self.__menedzer_motywow.ustaw_systemowy)

        self.akcja_jasny.triggered.connect(self.__menedzer_motywow.ustaw_jasny)
        self.akcja_jasny.triggered.connect(self.__ladowacz_ikon.zaladuj_ciemne_ikony)

        self.akcja_ciemny.triggered.connect(self.__menedzer_motywow.ustaw_ciemny)
        self.akcja_ciemny.triggered.connect(self.__ladowacz_ikon.zaladuj_jasne_ikony)

        self.akcja_wysoki_kontrast.triggered.connect(self.__menedzer_motywow.ustaw_wysoki_kontrast)
        self.akcja_wysoki_kontrast.triggered.connect(self.__ladowacz_ikon.zaladuj_kontrastowe_ikony)