from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class ElementListy(QWidget):
    def __init__(self, rodzic, rodzaj: str) -> None:
        super().__init__(rodzic)
        rozstawienie = QHBoxLayout(self)
        rozstawienie.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        nazwa = QLabel("Tutaj zdjęcie!", self)
        zdjecie = QLabel("Zdjecie1.jpg", self)
        rodzaj = QLabel(rodzaj, self)

        nazwa.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        zdjecie.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)
        rodzaj.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter)

        rozstawienie.addWidget(nazwa)
        rozstawienie.addWidget(zdjecie)
        rozstawienie.addWidget(rodzaj)