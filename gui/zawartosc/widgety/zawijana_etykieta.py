from PyQt6.QtWidgets import QLabel, QWidget, QSizePolicy
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtCore import Qt


class ZawijanaEtykieta(QLabel):
    def __init__(self, tekst: str, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.tekst = tekst
        self.__zawin_tekst(szerokosc=self.width())
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        self.setMinimumWidth(0)

    def resizeEvent(self, resize_event: QResizeEvent) -> None:
        super().resizeEvent(resize_event)
        nowy_rozmiar = resize_event.size().width()
        self.__zawin_tekst(nowy_rozmiar)

    def __zawin_tekst(self, szerokosc: int) -> None:
        tekst = self.fontMetrics().elidedText(self.tekst, Qt.TextElideMode.ElideRight, szerokosc)
        self.setText(tekst)

    def setText(self, nowy_tekst: str) -> None:
        super().setText(nowy_tekst)
        self.tekst = nowy_tekst

