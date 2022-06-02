import ntpath

from PyQt6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget, QSpacerItem, QHBoxLayout, QLayout
from PyQt6.QtCore import Qt, QThread, QObject, QSize
from PyQt6.QtGui import QPixmap, QResizeEvent

from .zawijana_etykieta import ZawijanaEtykieta
from .podglad_zdjecia import PodgladZdjecia


class ElementListy(QWidget):
    def __init__(self, sciezka: str, rodzaj: str) -> None:
        super().__init__()

        self.nazwa = ntpath.basename(sciezka)
        self.sciezka = sciezka
        self.rodzaj = rodzaj

        self.__rozstawienie = QHBoxLayout(self)
        self.__rozstawienie.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)

        self.__zdjecie = PodgladZdjecia(self.sciezka, self)
        self.__etykieta_nazwa = ZawijanaEtykieta(self.nazwa, self)
        self.__etykieta_rodzaj = ZawijanaEtykieta(self.rodzaj, self)

        self.__ustaw_wyrownanie()
        self.__ustaw_zawijanie_tekstu()
        self.__ustaw_rozciaganie()
        self.__dodaj_elementy()

    def __ustaw_wyrownanie(self) -> None:
        self.__etykieta_nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__etykieta_rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)

    def __ustaw_zawijanie_tekstu(self) -> None:
        # self.__etykieta_nazwa.setWordWrap(True)
        # self.__etykieta_rodzaj.setWordWrap(True)
        pass

    def __ustaw_rozciaganie(self) -> None:
        self.__etykieta_nazwa.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.__zdjecie.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.__etykieta_rodzaj.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

    def __dodaj_elementy(self) -> None:
        self.__rozstawienie.addWidget(self.__zdjecie)
        self.__rozstawienie.addWidget(self.__etykieta_nazwa)
        self.__rozstawienie.addWidget(self.__etykieta_rodzaj)


