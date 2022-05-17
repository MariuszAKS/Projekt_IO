from .designer.gui_designer import Ui_MainWindow
from .okno import GlowneOkno
from .widgety.element_listy import ElementListy
from ..logika.wybor_plikow import wybierz_pliki
from ..logika.imitacja_odczytywania_rodzaju import AnalizatorZdjec


class Ui(Ui_MainWindow):
    def __init__(self, glowne_okno: GlowneOkno) -> None:
        super().__init__()
        self.setupUi(glowne_okno)
        self.analizator = AnalizatorZdjec()
        self.przycisk_dodaj.clicked.connect(self.__analizuj_zdjecia)

    def __analizuj_zdjecia(self) -> None:
        sciezki = wybierz_pliki(self.obszar_przyciskow)
        self.__usun_stare_pozycje()
        self.analizator.analizuj_zdjecia(sciezki, self.__dodaj_pozycje)

    def __usun_stare_pozycje(self):
        lista_elementow = self.verticalLayout_2
        for i in reversed(range(lista_elementow.count())):
            lista_elementow.itemAt(i).setParent(None)

    def __dodaj_pozycje(self, sciezka_zdjecia: str, rodzaj: str) -> None:
        nowy_element = ElementListy(self.scrollAreaWidgetContents, sciezka_zdjecia, rodzaj)
        self.verticalLayout_2.addWidget(nowy_element)



