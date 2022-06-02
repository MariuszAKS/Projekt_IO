import ntpath
from typing import List, Tuple

from PyQt6.QtWidgets import QSizePolicy, QWidget, QHBoxLayout, QLayout
from PyQt6.QtCore import Qt

from .zawijana_etykieta import ZawijanaEtykieta
from .podglad_zdjecia import PodgladZdjecia


class ElementListy(QWidget):
    def __init__(self, sciezka: str, rodzaj: str) -> None:
        super().__init__()

        self.nazwa = ntpath.basename(sciezka)
        self.sciezka = sciezka
        self.rodzaj = rodzaj

        self.__zdjecie = PodgladZdjecia(self.sciezka, self)
        self.__etykieta_nazwa = ZawijanaEtykieta(self.nazwa, self)
        self.__etykieta_rodzaj = ZawijanaEtykieta(self.rodzaj, self)

        self.__ustaw_wyrownanie()
        self.__ustaw_rozciaganie()

        self.__rozstawienie = Rozstawienie(
            self.__zdjecie,
            self.__etykieta_nazwa,
            self.__etykieta_rodzaj,
            rodzic=self)

    def __ustaw_wyrownanie(self) -> None:
        self.__etykieta_nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__etykieta_rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)

    def __ustaw_rozciaganie(self) -> None:
        self.__etykieta_nazwa.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.__zdjecie.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.__etykieta_rodzaj.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)


class Rozstawienie(QHBoxLayout):
    def __init__(self, *widgety: QWidget, rodzic: QWidget):
        super().__init__(rodzic)
        self.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)

        for widget in widgety:
            self.addWidget(widget)