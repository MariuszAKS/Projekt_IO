"""
@package docstring
"""
import numpy as np
import skimage.io
from skimage.color import rgb2gray
from skimage.filters import thresholding
from skimage.filters import threshold_otsu
from skimage.util import img_as_ubyte


class ProgowanieOTSU:
    """
    Jest to klasa do generowania maski nakładanej później na obraz przy obliczaniu niektórych cech

    Maska ta ma na celu wyodrębnienie obszaru zainteresowania (bakterii) od tła
    """
    def __init__(self) -> None:
        """
        Konstruktor klasy
        """
        pass

    def maska(self, obraz: np.ndarray) -> np.ndarray:
        """
        Metoda służąca do wygenerowania maski obrazu
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        :return: Maska obrazu w postaci tablicy dwu-wymiarowej
        """
        skala_szarosci = rgb2gray(obraz)

        prog = threshold_otsu(skala_szarosci)
        wynik = skala_szarosci <= prog
        return wynik

    def zapisz_maske(self, obraz: np.ndarray, sciezka_wynik: str) -> np.ndarray:
        """
        Metoda służąca do zapisania maski w postaci pliku obrazu

        Metoda ta generuje maskę przed zapisem oraz zwraca ją poprzez return, więc może być stosowana zamiennie z metodą < maska(self, obraz) >
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        :param sciezka_wynik: Ścieżka do miejsca zapisu na dysku
        :return: Maska obrazu w postaci tablicy dwu-wymiarowej
        """
        wynik = self.maska(obraz)
        skimage.io.imsave(sciezka_wynik, img_as_ubyte(wynik))
        return wynik
