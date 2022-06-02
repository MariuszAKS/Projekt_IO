from typing import Callable
from ..designer.gui_designer import Ui_MainWindow
from ..okno import GlowneOkno
from ...logika.wybor_plikow import wybierz_pliki
from ...logika.odczytywanie_rodzaju import AnalizatorZdjec
from .menedzer_listy import MenedzerListy
from .stylizator import Stylizator


class Ui(Ui_MainWindow):
    def __init__(self, glowne_okno: GlowneOkno, funkcja_analizujaca: Callable[[str], str]) -> None:
        super().__init__()
        self.setupUi(glowne_okno)
        self.__analizator = AnalizatorZdjec(funkcja_analizujaca)
        self.stylizator = Stylizator(glowne_okno)
        self.__menedzer_listy = MenedzerListy(lista_elementow=self.verticalLayout_2)
        self.przycisk_dodaj.clicked.connect(self.__analizuj_zdjecia)
        self.przycisk_rodzaj.clicked.connect(self.__menedzer_listy.sortuj_po_rodzaju)
        self.przycisk_nazwa.clicked.connect(self.__menedzer_listy.sortuj_po_nazwie)

    def __analizuj_zdjecia(self) -> None:
        sciezki = wybierz_pliki(self.obszar_przyciskow)
        self.__analizator.analizuj_zdjecia(sciezki, self.__menedzer_listy.dodaj_pozycje)