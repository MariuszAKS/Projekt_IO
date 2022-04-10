from PyQt6.QtWidgets import *

class ElementListy(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        rozstawienie = QHBoxLayout()
        self.setLayout(rozstawienie)
        rozstawienie.addWidget(QLabel("Tutaj zdjęcie!", self))
        rozstawienie.addWidget(QLabel("Zdjecie1.jpg", self))
        rozstawienie.addWidget(QLabel("Cumulumbulus",self))