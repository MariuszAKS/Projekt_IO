from operator import imod
from PyQt6.QtWidgets import *
import sys
from gui import *



app = QApplication(sys.argv)
window = QMainWindow()

window.setGeometry(200, 200, 800, 600)
window.setWindowTitle("Tytuł okna")

ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec())
