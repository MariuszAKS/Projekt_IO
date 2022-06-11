"""
@package docstring
"""
import numpy as np
from skimage.color import rgb2lab
from sklearn.cluster import KMeans
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils._testing import ignore_warnings

from typing import List


class KlastryKSrednich:
    """
    Jest to klasa do obliczania centroidów klastra pikseli obrazu w przestrzeni lab
    """
    def __init__(self, obraz: np.ndarray) -> None:
        """
        Konstruktor kopiujący inicjalizujący wszystkie pola składowe klasy
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        """
        self.obr = rgb2lab(obraz, "D65", "2")
        self.__obl_klastry()

    def zmien_obraz(self, obraz: np.ndarray) -> None:
        """
        Metoda służąca do zmiany obrazu
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        """
        self.obr = rgb2lab(obraz, "D65", "2")
        self.__obl_klastry()

    @ignore_warnings(category=ConvergenceWarning)
    def __obl_klastry(self) -> None:
        """
        Metoda służąca do obliczenia centroid klastra b*
        """
        b = np.array([[x] for x in self.obr[:, :, 2].flatten()])
        self.k_srednich_b = KMeans(n_clusters=3).fit(b)

    def centroidy_b(self) -> List[float]:
        """
        Metoda zwracająca centroidy klastra b*
        """
        return self.k_srednich_b.cluster_centers_

    # zapisuje wizualizacje klastrów
    # sciezka_wynik = ścieżka do pliku
    # def zapisz_klaster_obraz_a(self, sciezka_wynik):
    #     kl = self.k_srednich_a.labels_
    #     kl = np.reshape(kl, (self.obr.shape[0], self.obr.shape[1])) * 127
    #     skimage.io.imsave(sciezka_wynik, img_as_ubyte(kl), check_contrast=False)

    # zapisuje wizualizacje klastrów
    # sciezka_wynik = ścieżka do pliku
    # def zapisz_klaster_obraz_b(self, sciezka_wynik):
    #     kl = self.k_srednich_b.labels_
    #     kl = np.reshape(kl, (self.obr.shape[0], self.obr.shape[1])) * 127
    #     skimage.io.imsave(sciezka_wynik, img_as_ubyte(kl), check_contrast=False)
