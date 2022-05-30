import ntpath

from PyQt6.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget, QSpacerItem
from PyQt6.QtCore import Qt, QThread, QObject
from PyQt6.QtGui import QPixmap, QResizeEvent


class ElementListy(QWidget):
    def __init__(self, sciezka: str, rodzaj: str) -> None:
        super().__init__()

        self.nazwa = ntpath.basename(sciezka)
        self.sciezka = sciezka
        self.rodzaj = rodzaj

        self.__rozstawienie = QGridLayout(self)
        self.__zdjecie = _Podglad_zdjecia(self.sciezka, self)
        self.__etykieta_nazwa = _Zawijana_etykieta(self.nazwa, self)
        self.__etykieta_rodzaj = _Zawijana_etykieta(self.rodzaj, self)

        # self.__rozstawienie.setStyleSheet("padding: 10px")

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


        # spacer1 = Q




        self.__rozstawienie.addWidget(self.__zdjecie)
        self.__rozstawienie.addWidget(self.__etykieta_nazwa)
        self.__rozstawienie.addWidget(self.__etykieta_rodzaj)


class _Podglad_zdjecia(QLabel):
    def __init__(self, sciezka: str, rodzic: ElementListy) -> None:
        super().__init__(rodzic)
        self.__pixmapa = QPixmap(sciezka)
        self.show()

    def resizeEvent(self, resize_event: QResizeEvent) -> None:
        margines = 1  # pixmapa nie może zajmować całej dostępnej przestrzeni bo layout nigdy nie będzie chciał jej zmniejszać
        # nowy_rozmiar = resizeEvent.size().width() - margines
        nowy_rozmiar = self.width()-20
        zeskalowana_pixmapa = self.__pixmapa.scaledToWidth(nowy_rozmiar)
        self.setPixmap(zeskalowana_pixmapa)


        return super().resizeEvent(resize_event)


class _Zawijana_etykieta(QLabel):
    def __init__(self, tekst, rodzic):
        super().__init__(rodzic)
        self.tekst = tekst
        self.setText(tekst)

    def resizeEvent(self, resize_event: QResizeEvent) -> None:
        tekst = self.text()
        dlugosc_tekstu = self.fontMetrics().boundingRect(tekst).width()

        print(dlugosc_tekstu)
        if dlugosc_tekstu > resize_event.size().width():
            self.setText(self.tekst[:3] + "...")

        return super().resizeEvent(resize_event)
