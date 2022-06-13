from PyQt6.QtWidgets import QLabel, QSizePolicy, QWidget
from PyQt6.QtGui import QPixmap, QResizeEvent


class PodgladZdjecia(QLabel):
    '''Widżet wyświetlający podgląd zdjęcia'''

    def __init__(self, sciezka_zdjecia: str, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Maximum)

        self.setPixmap(QPixmap(sciezka_zdjecia))
        self.setScaledContents(True)

    def resizeEvent(self, resize_event: QResizeEvent) -> None:
        super().resizeEvent(resize_event)

        pixmapa = self.pixmap()

        try:
            proporcje = pixmapa.height() / pixmapa.width()
        except ZeroDivisionError:
            proporcje = 1

        szerokosc = self.width()
        wysokosc = int(szerokosc*proporcje)

        self.setMinimumHeight(wysokosc)
        self.setMaximumHeight(wysokosc)