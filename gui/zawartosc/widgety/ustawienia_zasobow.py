from multiprocessing import cpu_count

from PyQt6.QtWidgets import QDialog, QMainWindow
from PyQt6.QtCore import Qt

from ...logika.wielowatkowosc.analizator_zdjec import AnalizatorZdjec
from ..designer.ustawienia_zasobow_designer import Ui_Dialog

class UstawieniaZasobow(QDialog):
    '''Okno ustawień zużycia zasobów'''

    def __init__(self, glowne_okno: QMainWindow, analizator: AnalizatorZdjec) -> None:
        super().__init__()

        self.resize(800, 200)
        self.__glowne_okno = glowne_okno
        self.__analizator = analizator

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Ustawienia zasobów")

        self.ui.suwak.setMaximum(cpu_count())
        self.ui.suwak.valueChanged.connect(lambda: self.ui.wartosc.setText(str(self.ui.suwak.value())))
        self.ui.suwak.valueChanged.connect(lambda: self.__analizator.zmien_limit_procesow(self.ui.suwak.value()))

    def otworz(self):
        '''Otwiera okno z ustawieniami zużycia zasobów'''

        self.setStyleSheet(self.__glowne_okno.styleSheet())
        self.ui.suwak.setValue(self.__analizator.maks_liczba_procesow)

        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.exec()