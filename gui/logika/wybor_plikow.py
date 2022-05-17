from typing import List

from PyQt6.QtWidgets import QFileDialog, QWidget

def wybierz_pliki(rodzic: QWidget) -> List[str]:
    sciezki = QFileDialog().getOpenFileNames(rodzic, 'Wybierz zdjęcia', 'C:\\', 'Image files (*.png)')
    return sciezki[0]