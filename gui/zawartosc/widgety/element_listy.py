import ntpath

from PyQt6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QResizeEvent


class ElementListy(QWidget):
    def __init__(self, sciezka: str, rodzaj: str) -> None:
        super().__init__()

        self.nazwa = ntpath.basename(sciezka)
        self.sciezka = sciezka
        self.rodzaj = rodzaj

        rozstawienie = QGridLayout(self)
        rozstawienie.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        zdjecie = _Podglad_zdjecia(self.sciezka, self)
        etykieta_nazwa = QLabel(self.nazwa, self)
        etykieta_rodzaj = QLabel(self.rodzaj, self)

        etykieta_nazwa.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        zdjecie.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        etykieta_rodzaj.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        etykieta_nazwa.setWordWrap(True)
        etykieta_rodzaj.setWordWrap(True)

        etykieta_nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        etykieta_rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)

        rozstawienie.setColumnStretch(0, 1)
        rozstawienie.setColumnStretch(1, 1)
        rozstawienie.setColumnStretch(2, 1)

        rozstawienie.addWidget(zdjecie)
        rozstawienie.addWidget(etykieta_nazwa)
        rozstawienie.addWidget(etykieta_rodzaj)


class _Podglad_zdjecia(QLabel):
    def __init__(self, sciezka, rodzic):
        super().__init__(rodzic)
        self.__pixmapa = QPixmap(sciezka)
        self.setPixmap(self.__pixmapa.scaledToWidth(200))
        self.show()

    def resizeEvent(self, resizeEvent: QResizeEvent) -> None:
        margines = 1  # pixmapa nie moze zajmowac calej dostepnej przestrzeni bo layout nigdy nie bedzie chcial jej zmniejszac
        zeskalowana_pixmapa = self.__pixmapa.scaledToWidth(resizeEvent.size().width()-margines)
        self.setPixmap(zeskalowana_pixmapa)
        self.show()
        return super().resizeEvent(resizeEvent)