from PyQt6.QtWidgets import QLabel, QWidget, QSizePolicy
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtCore import Qt


class ZawijanaEtykieta(QLabel):
    MIN_SZEROKOSC = 1

    def __init__(self, tekst: str, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.tekst = tekst
        self.__ustaw_tekst(szerokosc=self.width())
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        self.setMinimumWidth(0)

    def resizeEvent(self, resize_event: QResizeEvent) -> None:
        super().resizeEvent(resize_event)
        nowy_rozmiar = resize_event.size().width()
        self.__ustaw_tekst(nowy_rozmiar)

    def __ustaw_tekst(self, szerokosc: int) -> None:
        tekst = self.fontMetrics().elidedText(self.tekst, Qt.TextElideMode.ElideRight, szerokosc)
        self.setText(tekst)