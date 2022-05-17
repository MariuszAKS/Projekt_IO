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

        self.__rozstawienie = QGridLayout(self)
        self.__zdjecie = _Podglad_zdjecia(self.sciezka, self)
        self.__etykieta_nazwa = QLabel(self.nazwa, self)
        self.__etykieta_rodzaj = QLabel(self.rodzaj, self)

        self.__ustaw_wyrownanie()
        self.__ustaw_zawijanie_tekstu()
        self.__ustaw_proporcje()
        self.__dodaj_elementy()

    def __ustaw_wyrownanie(self) -> None:
        self.__etykieta_nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        self.__etykieta_rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)

    def __ustaw_zawijanie_tekstu(self) -> None:
        self.__etykieta_nazwa.setWordWrap(True)
        self.__etykieta_rodzaj.setWordWrap(True)

    def __ustaw_proporcje(self) -> None:
        self.__etykieta_nazwa.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.__zdjecie.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.__etykieta_rodzaj.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.__rozstawienie.setColumnStretch(0, 1)
        self.__rozstawienie.setColumnStretch(1, 1)
        self.__rozstawienie.setColumnStretch(2, 1)

    def __dodaj_elementy(self) -> None:
        self.__rozstawienie.addWidget(self.__zdjecie)
        self.__rozstawienie.addWidget(self.__etykieta_nazwa)
        self.__rozstawienie.addWidget(self.__etykieta_rodzaj)


class _Podglad_zdjecia(QLabel):
    def __init__(self, sciezka: str, rodzic: ElementListy) -> None:
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