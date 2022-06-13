from PyQt6.QtWidgets import QLabel, QWidget, QSizePolicy
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtCore import Qt


class ZawijanaEtykieta(QLabel):
    '''Widzet będący etykietą, w której tekst jest chowany jeśli wykracza poza jej rozmiar'''

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

    def ustaw_pelna_nazwe(self, nowa_nazwa: str) -> None:
        '''Ustawia pełną treść etykiety'''

        self.tekst = nowa_nazwa
        self.__zawin_tekst(self.width())

    def __zawin_tekst(self, szerokosc: int) -> None:
        """
        Chowa tekst wykraczająćy poza podaną szerokość
        :param szerokosc: Szerokość w jakiej ma zmieścić się tekst
        """

        tekst = self.fontMetrics().elidedText(self.tekst, Qt.TextElideMode.ElideRight, szerokosc)
        self.setText(tekst)

