from PyQt6.QtWidgets import *

def wybierz_pliki(rodzic):
    okno = QFileDialog().getOpenFileNames(rodzic,'Wybierz zdjęcia', 'C:\\', 'Image files (*.jpg)')
    return okno[0]