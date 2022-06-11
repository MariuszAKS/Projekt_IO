"""
@package docstring
"""
import numpy as np
from skimage.color import rgb2gray
from skimage.feature import canny

from typing import List


class Krawedzie:
    """
    Jest to klasa do obliczania cech na wykrytych krawędziach obrazu
    """
    def __init__(self, obraz: np.ndarray) -> None:
        """
        Konstruktor kopiujący inicjalizujący wszystkie pola składowe klasy
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        """
        self.obr_kolor = obraz
        obr = rgb2gray(self.obr_kolor)
        self.maska_krawedzi = canny(obr, sigma=1)

    def zmien_obraz(self, obraz: np.ndarray) -> None:
        """
        Metoda służąca do zmiany obrazu
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        """
        self.obr_kolor = obraz
        obr = rgb2gray(self.obr_kolor)
        self.maska_krawedzi = canny(obr, sigma=1)

    def maska(self) -> np.ndarray:
        """
        Metoda zwracająca maskę krawędzi
        """
        return self.maska_krawedzi

    def gestosc_krawedzi(self) -> float:
        """
        Metoda służąca do obliczenia gęstości wykrytych krawędzi na obrazie
        """
        return np.count_nonzero(self.maska_krawedzi) / (self.maska_krawedzi.shape[0] * self.maska_krawedzi.shape[1])

    def sredni_kolor_krawedzi_rgb_r(self) -> float:
        """
        Metoda służąca do obliczenia średniej w przestrzeni kolorów rgb
        :return: Wartość średniej koloru zielonego
        """
        r = self.obr_kolor[:, :, 0]  # czerwony
        r = r[self.maska_krawedzi]
        if len(r) == 0:
            return 0
        return r.mean()

    def std_kolor_krawedzi_rgb(self) -> List:
        """
        Metoda służąca do obliczenia odchylenia standardowego w przestrzeni kolorów rgb
        :return: Wartości odchyleń standardowych kolorów czerwonego, zielonego i niebieskiego
        """
        r = self.obr_kolor[:, :, 0]  # czerwony
        g = self.obr_kolor[:, :, 1]  # zielony
        b = self.obr_kolor[:, :, 2]  # niebieski
        return [r[self.maska_krawedzi].std(), g[self.maska_krawedzi].std(), b[self.maska_krawedzi].std()]
