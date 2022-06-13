from typing import List

from PyQt6.QtWidgets import QFileDialog, QWidget

def wybierz_pliki(rodzic: QWidget) -> List[str]:
    """
    Otwiera okno do wyboru plików do otworzenia
    :param rodzic: Widżet nadrzędny
    :return: Lista ścieżek do wybranych plików
    """

    sciezki = QFileDialog().getOpenFileNames(rodzic, 'Wybierz zdjęcia', 'C:\\', 'Pliki obrazów (*.png)')
    return sciezki[0]