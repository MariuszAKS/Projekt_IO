from PyQt6.QtWidgets import QLabel, QSizePolicy, QWidget
from PyQt6.QtGui import QResizeEvent, QPixmap


class PodgladZdjecia(QLabel):
    MIN_SZEROKOSC = 1

    def __init__(self, sciezka: str, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.setMinimumWidth(0)
        self.__pixmapa = QPixmap(sciezka)
        self.setPixmap(self.__pixmapa)
        self.show()

    def resizeEvent(self, resize_event: QResizeEvent) -> None:
        super().resizeEvent(resize_event)
        nowa_szerokosc = self.width()

        if nowa_szerokosc > PodgladZdjecia.MIN_SZEROKOSC:
            nowa_szerokosc -= 1

        zeskalowana_pixmapa = self.__pixmapa.scaledToWidth(nowa_szerokosc)
        self.setPixmap(zeskalowana_pixmapa)