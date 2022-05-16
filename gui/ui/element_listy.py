from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from ui.gui import Ui_MainWindow

class ElementListy(QWidget):
    def __init__(self, rodzic, nazwa: str, zdjecie: str, rodzaj: str) -> None:
        super().__init__(rodzic)
        # rozstawienie = QHBoxLayout(self)
        rozstawienie = QGridLayout(self)
        rozstawienie.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        nazwa = QLabel(nazwa, self)
        zdjecie = QLabel(zdjecie, self)
        rodzaj = QLabel(rodzaj, self)

        nazwa.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        zdjecie.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        rodzaj.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        nazwa.setWordWrap(True)
        zdjecie.setWordWrap(True)
        rodzaj.setWordWrap(True)


        nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)

        rozstawienie.setColumnStretch(0, 1)
        rozstawienie.setColumnStretch(1, 1)
        rozstawienie.setColumnStretch(2, 1)

        rozstawienie.addWidget(zdjecie)
        rozstawienie.addWidget(nazwa)
        rozstawienie.addWidget(rodzaj)



def dodaj_pozycje(ui: Ui_MainWindow, nazwa: str, zdjecie: str, rodzaj: str):
    ui.verticalLayout_2.addWidget(ElementListy(ui.scrollAreaWidgetContents, nazwa, zdjecie, rodzaj))