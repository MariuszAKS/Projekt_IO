from PyQt6.QtWidgets import *

def wybierz_pliki(rodzic):
    okno = QFileDialog().getOpenFileNames(rodzic,'Wybierz zdjęcia', 'C:\\', 'Image files (*.png)')
    return okno[0]