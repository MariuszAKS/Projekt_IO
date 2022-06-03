import ntpath

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLayout
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtCore import Qt

from .zawijana_etykieta import ZawijanaEtykieta
from .podglad_zdjecia import PodgladZdjecia


class ElementListy(QWidget):
    def __init__(self, sciezka: str, rodzaj: str) -> None:
        super().__init__()

        self.nazwa = ntpath.basename(sciezka)
        self.sciezka = sciezka
        self.rodzaj = rodzaj

        self.zdjecie = PodgladZdjecia(self.sciezka, self)
        self.__etykieta_nazwa = ZawijanaEtykieta(self.nazwa, self)
        self.__etykieta_rodzaj = ZawijanaEtykieta(self.rodzaj, self)

        self.__ustaw_wyrownanie()

        self.__rozstawienie = Rozstawienie(
            self.zdjecie,
            self.__etykieta_nazwa,
            self.__etykieta_rodzaj,
            rodzic=self)

    def __ustaw_wyrownanie(self) -> None:
        self.__etykieta_nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__etykieta_rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)


class Rozstawienie(QHBoxLayout):
    def __init__(self, *widgety: QWidget, rodzic: QWidget):
        super().__init__(rodzic)
        self.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)

        for widget in widgety:
            self.addWidget(widget)