from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QResizeEvent
from ui.gui import Ui_MainWindow

class ElementListy(QWidget):
    def __init__(self, rodzic, sciezka: str, zdjecie: str, rodzaj: str) -> None:
        super().__init__(rodzic)

        rozstawienie = QGridLayout(self)
        rozstawienie.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        zdjecie = _Podglad_zdjecia(sciezka, self)
        sciezka = QLabel(sciezka, self)
        rodzaj = QLabel(rodzaj, self)

        sciezka.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        zdjecie.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        rodzaj.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        sciezka.setWordWrap(True)
        rodzaj.setWordWrap(True)

        sciezka.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)

        rozstawienie.setColumnStretch(0, 1)
        rozstawienie.setColumnStretch(1, 1)
        rozstawienie.setColumnStretch(2, 1)

        rozstawienie.addWidget(zdjecie)
        rozstawienie.addWidget(sciezka)
        rozstawienie.addWidget(rodzaj)


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



def dodaj_pozycje(ui: Ui_MainWindow, nazwa: str, zdjecie: str, rodzaj: str):
    ui.verticalLayout_2.addWidget(ElementListy(ui.scrollAreaWidgetContents, nazwa, zdjecie, rodzaj))