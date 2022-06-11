"""
@package docstring
"""
import numpy as np
import skimage.io
import skimage.color

from typing import List


class CechyKolorymetryczne:
    """
    Jest to klasa do obliczania cech kolorymetrycznych obrazu
    """
    def __init__(self, obraz: np.ndarray, maska: np.ndarray) -> None:
        """
        Konstruktor kopiujący inicjalizujący wszystkie pola składowe klasy
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        :param maska: Przechowuje maske w postaci tablicy dwu-wymiarowej
        """
        self.obraz = obraz
        self.maska = maska

    def zmien_obraz(self, obraz: np.ndarray, maska: np.ndarray) -> None:
        """
        Metoda służąca do zmiany obrazu
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        :param maska: Przechowuje maske w postaci tablicy dwu-wymiarowej
        """
        self.obraz = obraz
        self.maska = maska

    def srednia_rgb_g(self) -> float:
        """
        Metoda służąca do obliczenia średniej w przestrzeni kolorów rgb
        :return: Wartość średniej koloru zielonego
        """
        wartosc = 0.0
        licznik = 0
        for i in range(0, self.obraz.shape[0]):
            for j in range(0, self.obraz.shape[1]):
                if self.maska[i, j]:
                    wartosc += self.obraz[i, j, 1]
                    licznik += 1
        wynik = wartosc/licznik
        return wynik

    def srednia_hsv_sv(self) -> List[float]:
        """
        Metoda służąca do obliczenia średniej w przestrzeni kolorów hsv
        :return: Wartości średnich nasycenia i wartości
        """
        hsv_obr = skimage.color.rgb2hsv(self.obraz)
        wynik = []
        for kanal in range(1, 3):
            wartosc = 0.0
            licznik = 0
            for i in range(0, hsv_obr.shape[0]):
                for j in range(0, hsv_obr.shape[1]):
                    if self.maska[i, j]:
                        wartosc += hsv_obr[i, j, kanal]
                        licznik += 1
            wynik.append(wartosc/licznik)
        return wynik

    def srednia_lab_l(self) -> float:
        """
        Metoda służąca do obliczenia średniej w przestrzeni kolorów lab
        :return: Wartość średniej luminacji
        """
        lab_obr = skimage.color.rgb2lab(self.obraz, "D65", "2")
        wartosc = 0.0
        licznik = 0
        for i in range(0, lab_obr.shape[0]):
            for j in range(0, lab_obr.shape[1]):
                if self.maska[i, j]:
                    wartosc += lab_obr[i, j, 0]
                    licznik += 1
        wynik = wartosc/licznik
        return wynik

    def std_rgb(self) -> List[float]:
        """
        Metoda służąca do obliczenia odchylenia standardowego w przestrzeni kolorów rgb
        :return: Wartości odchyleń standardowych kolorów czerwonego, zielonego i niebieskiego
        """
        wynik = []
        r = self.obraz[:, :, 0]  # czerwony
        g = self.obraz[:, :, 1]  # zielony
        b = self.obraz[:, :, 2]  # niebieski

        wynik.append(np.std(r[self.maska]))
        wynik.append(np.std(g[self.maska]))
        wynik.append(np.std(b[self.maska]))
        return wynik

    def std_hsv_v(self) -> float:
        """
        Metoda służąca do obliczenia odchylenia standardowego w przestrzeni kolorów hsv
        :return: Wartość odchylenia standardowego wartości
        """
        hsv_obr = skimage.color.rgb2hsv(self.obraz)
        v = hsv_obr[:, :, 2]  # wartosc

        wynik = np.std(v[self.maska])
        return wynik

    def std_lab_la(self) -> List[float]:
        """
        Metoda służąca do obliczenia odchylenia standardowego w przestrzeni kolorów lab
        :return: Wartości odchyleń standardowych luminacji i tinty
        """
        lab_obr = skimage.color.rgb2lab(self.obraz, "D65", "2")
        wynik = []
        l = lab_obr[:, :, 0]  # luminacja
        a = lab_obr[:, :, 1]  # tienta

        wynik.append(np.std(l[self.maska]))
        wynik.append(np.std(a[self.maska]))
        return wynik
