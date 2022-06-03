from PyQt6.QtWidgets import QLabel, QSizePolicy, QWidget
from PyQt6.QtGui import QPixmap


class PodgladZdjecia(QLabel):
    def __init__(self, sciezka: str, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Maximum)
        self.setPixmap(QPixmap(sciezka))
        self.setScaledContents(True)

