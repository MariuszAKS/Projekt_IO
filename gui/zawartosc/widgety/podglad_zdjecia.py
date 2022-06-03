from PyQt6.QtWidgets import QLabel, QSizePolicy, QWidget
from PyQt6.QtGui import QPixmap


class PodgladZdjecia(QLabel):
    MIN_SZEROKOSC = 1

    def __init__(self, sciezka: str, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Maximum)
        self.setPixmap(QPixmap(sciezka))
        self.show()
        self.setScaledContents(True)