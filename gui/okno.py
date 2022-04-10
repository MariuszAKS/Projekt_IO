from operator import imod
from PyQt6.QtWidgets import *
import sys
from gui import Ui_MainWindow
from element_listy import ElementListy


aplikacja = QApplication(sys.argv)
okno = QMainWindow()

okno.setGeometry(200, 200, 800, 600)
okno.setWindowTitle("Tytuł okna")

ui = Ui_MainWindow()
ui.setupUi(okno)

okno.show()
sys.exit(aplikacja.exec())