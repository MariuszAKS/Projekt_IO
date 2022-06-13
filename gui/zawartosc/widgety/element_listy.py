import ntpath

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLayout
from PyQt6.QtCore import Qt

from .zawijana_etykieta import ZawijanaEtykieta
from .podglad_zdjecia import PodgladZdjecia


class ElementListy(QWidget):
    '''Widżet pojedynczej pozycji na głównej liście elementów w GUI'''

    def __init__(self, sciezka_zdjecia: str) -> None:
        super().__init__()

        self.nazwa = ntpath.basename(sciezka_zdjecia)[:-4]
        self.sciezka = sciezka_zdjecia
        self.rodzaj = "Analizowanie..."

        self.zdjecie = PodgladZdjecia(self.sciezka, self)
        self.__etykieta_nazwa = ZawijanaEtykieta(self.nazwa, self)
        self.__etykieta_rodzaj = ZawijanaEtykieta(self.rodzaj, self)

        self.__ustaw_wyrownanie()

        self.__rozstawienie = Rozstawienie(
            self.zdjecie,
            self.__etykieta_nazwa,
            self.__etykieta_rodzaj,
            rodzic=self)

    def ustaw_rodzaj(self, rodzaj: str) -> None:
        self.rodzaj = rodzaj
        self.__etykieta_rodzaj.ustaw_pelna_nazwe(rodzaj)

    def __ustaw_wyrownanie(self) -> None:
        '''Ustawia wyrównanie elementów'''

        self.__etykieta_nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__etykieta_rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)


class Rozstawienie(QHBoxLayout):
    '''Odpowiednio rozstawia elementy'''

    def __init__(self, *widgety: QWidget, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)

        for widget in widgety:
            self.addWidget(widget)