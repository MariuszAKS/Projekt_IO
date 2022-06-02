from PyQt6.QtWidgets import QLabel, QWidget, QSizePolicy
from PyQt6.QtGui import QResizeEvent, QPaintEvent, QPainter
from PyQt6.QtCore import Qt


class ZawijanaEtykieta(QLabel):
    def __init__(self, tekst: str, rodzic: QWidget) -> None:
        super().__init__(rodzic)
        self.tekst = tekst
        self.__ustaw_tekst(szerokosc=self.width())
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.setMinimumWidth(0)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        metrics = self.fontMetrics()
        tekst = metrics.elidedText(self.tekst, Qt.TextElideMode.ElideRight, self.width())
        painter.drawText(self.frameRect(), self.alignment(), tekst)

    # def resizeEvent(self, resize_event: QResizeEvent) -> None:
    #     super().resizeEvent(resize_event)
    #     self.__ustaw_tekst(szerokosc=max(resize_event.size().width()-10, 1))

    def __ustaw_tekst(self, szerokosc: int) -> None:
        tekst = self.fontMetrics().elidedText(self.tekst, Qt.TextElideMode.ElideRight, szerokosc)
        self.setText(tekst)