from PyQt6.QtWidgets import *
import sys
from ui.gui import Ui_MainWindow
from logika.imitacja_odczytywania_rodzaju import ustaw_dodawanie


aplikacja = QApplication(sys.argv)
okno = QMainWindow()

okno.setGeometry(200, 200, 800, 600)
okno.setWindowTitle("Tytuł okna")

ui = Ui_MainWindow()
ui.setupUi(okno)
ustaw_dodawanie(ui)

okno.show()
sys.exit(aplikacja.exec())