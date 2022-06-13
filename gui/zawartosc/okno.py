from typing import Callable

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QCloseEvent, QIcon

class GlowneOkno(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowIcon(QIcon("gui/zasoby/ikony/aplikacja.png"))
        self.__gdy_zamkniete = None
        self.setGeometry(0, 0, 800, 600)
        self.showMaximized()
        self.show()

    def ustaw_gdy_zamkniete(self, funkcja: Callable) -> None:
        self.__gdy_zamkniete = funkcja

    def closeEvent(self, event: QCloseEvent) -> None:
        self.__gdy_zamkniete
        super().closeEvent(event)
