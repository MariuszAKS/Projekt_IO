"""
@package docstring
"""
import math
import numpy as np
import skimage.color
import skimage.io
from skimage.measure.entropy import shannon_entropy

from typing import List


class CechyHistogram:
    """
    Jest to klasa do obliczania wartości cech obrazu związanych z jego histogramem
    """
    def __init__(self, obraz: np.ndarray, maska: np.ndarray) -> None:
        """
        Konstruktor kopiujący inicjalizujący wszystkie pola składowe klasy
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        :param maska: Przechowuje maske w postaci tablicy dwu-wymiarowej
        """
        self.obr = obraz
        self.maska = maska
        self.__obl_hist()

    def zmien_obraz(self, obraz: np.ndarray, maska: np.ndarray) -> None:
        """
        Metoda służąca do zmiany obrazu
        :param obraz: Przechowuje obraz w postaci tablicy wielowymiarowej
        :param maska: Przechowuje maske w postaci tablicy dwu-wymiarowej
        """
        # if type(obraz) == str:
        #     self.obr = skimage.io.imread(obraz)
        self.obr = obraz
        self.maska = maska
        self.__obl_hist()

    # wylicza histogramy, wywoływane w konstruktorze/zmien_obraz
    def __obl_hist(self) -> None:
        """
        Metoda służąca do obliczenia cech kolorymetrycznych histogramu dla różnych przestrzeni kolorów

        Metoda wywoływana w konstruktorze oraz przy zmianie obrazu
        """
        r = self.obr[:, :, 0]  # kolor czerwony
        g = self.obr[:, :, 1]  # kolor zielony
        self.hist_r, bin_brzegi_r = np.histogram(r[self.maska], bins=256, range=(0, 256))
        self.hist_g, bin_brzegi_g = np.histogram(g[self.maska], bins=256, range=(0, 256))
        self.mids_r = bin_brzegi_r[:-1]
        self.mids_g = bin_brzegi_g[:-1]

        hsv_obr = skimage.color.rgb2hsv(self.obr)
        s = hsv_obr[:, :, 1]  # nasycenie
        v = hsv_obr[:, :, 2]  # wartosc
        self.hist_s, bin_brzegi_s = np.histogram(s[self.maska], bins=100, range=(0, 1))
        self.hist_v, bin_brzegi_v = np.histogram(v[self.maska], bins=100, range=(0, 1))
        self.mids_s = 0.5*(bin_brzegi_s[1:] + bin_brzegi_s[:-1])
        self.mids_v = 0.5*(bin_brzegi_v[1:] + bin_brzegi_v[:-1])

        lab_obr = skimage.color.rgb2lab(self.obr, "D65", "2")
        l = lab_obr[:, :, 0]  # luminacja
        a = lab_obr[:, :, 1]  # tienta
        b = lab_obr[:, :, 2]  # temperatura
        self.hist_l, bin_brzegi_l = np.histogram(l[self.maska], bins=100, range=(0, 100))
        self.hist_a, bin_brzegi_a = np.histogram(a[self.maska], bins=256, range=(-128, 128))
        self.hist_b, bin_brzegi_b = np.histogram(b[self.maska], bins=256, range=(-128, 128))
        self.mids_l = 0.5*(bin_brzegi_l[1:] + bin_brzegi_l[:-1])
        self.mids_a = 0.5*(bin_brzegi_a[1:] + bin_brzegi_a[:-1])
        self.mids_b = 0.5*(bin_brzegi_b[1:] + bin_brzegi_b[:-1])

        self.mean_r = 0.0 if sum(self.hist_r) == 0 else np.average(self.mids_r, weights=self.hist_r)
        self.mean_g = 0.0 if sum(self.hist_g) == 0 else np.average(self.mids_g, weights=self.hist_g)

        self.mean_s = 0.0 if sum(self.hist_s) == 0 else np.average(self.mids_s, weights=self.hist_s)
        self.mean_v = 0.0 if sum(self.hist_v) == 0 else np.average(self.mids_v, weights=self.hist_v)

        self.mean_l = 0.0 if sum(self.hist_l) == 0 else np.average(self.mids_l, weights=self.hist_l)
        self.mean_a = 0.0 if sum(self.hist_a) == 0 else np.average(self.mids_a, weights=self.hist_a)

    def hist_srednia_rgb_g(self) -> float:
        """
        Metoda zwracająca średnie w przestrzeni kolorów rgb
        :return: Wartość średniej koloru zielonego
        """
        return self.mean_g

    def hist_srednia_hsv_sv(self) -> List:

        """
        Metoda zwracająca średnie w przestrzeni kolorów hsv
        :return: Wartości średnich nasycenia i wartości
        """
        return [self.mean_s, self.mean_v]

    def hist_srednia_lab_l(self) -> float:
        """
        Metoda zwracająca średnie w przestrzeni kolorów lab
        :return: Wartość średniej luminacji
        """
        return self.mean_l

    def hist_var_rgb_rg(self) -> List:
        """
        Metoda służąca do obliczenia wariancji w przestrzeni kolorów rgb
        :return: Wartości średnich kolorów czerwonego i zielonego
        """
        wynik = []
        wynik.append(0.0 if sum(self.hist_r) == 0 else np.average((self.mids_r - self.mean_r)**2, weights=self.hist_r))
        wynik.append(0.0 if sum(self.hist_g) == 0 else np.average((self.mids_g - self.mean_g)**2, weights=self.hist_g))
        print(wynik)
        return wynik

    def hist_var_hsv_v(self) -> float:
        """
        Metoda służąca do obliczenia wariancji w przestrzeni kolorów hsv
        :return: Wartość średniej wartości
        """
        wynik = 0.0 if sum(self.hist_v) == 0 else np.average((self.mids_v - self.mean_v)**2, weights=self.hist_v)
        return wynik

    def hist_var_lab_la(self) -> List:
        """
        Metoda służąca do obliczenia wariancji w przestrzeni kolorów lab
        :return: Wartości średnich luminacji i tinty
        """
        wynik = []
        wynik.append(0.0 if sum(self.hist_l) == 0 else np.average((self.mids_l - self.mean_l)**2, weights=self.hist_l))
        wynik.append(0.0 if sum(self.hist_a) == 0 else np.average((self.mids_a - self.mean_a)**2, weights=self.hist_a))
        return wynik

    def hist_skos_rgb_rg(self) -> List:
        """
        Metoda służąca do obliczenia skośności w przestrzeni kolorów rgb
        :return: Wartości skośności kolorów czerwonego i zielonego
        """
        wynik = []
        wynik.append((np.sum((self.hist_r-self.mean_r)**3)/self.hist_r.size)/math.sqrt((np.sum((self.hist_r-self.mean_r)**2)/self.hist_r.size)**3))
        wynik.append((np.sum((self.hist_g-self.mean_g)**3)/self.hist_g.size)/math.sqrt((np.sum((self.hist_g-self.mean_g)**2)/self.hist_g.size)**3))
        return wynik

    def hist_skos_hsv_sv(self) -> List:
        """
        Metoda służąca do obliczenia skośności w przestrzeni kolorów hsv
        :return: Wartości skośności nasycenia i wartości
        """
        wynik = []
        wynik.append((np.sum((self.hist_s-self.mean_s)**3)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-self.mean_s)**2)/self.hist_s.size)**3))
        wynik.append((np.sum((self.hist_v-self.mean_v)**3)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-self.mean_v)**2)/self.hist_v.size)**3))
        return wynik

    def hist_skos_lab_la(self) -> List:
        """
        Metoda służąca do obliczenia skośności w przestrzeni kolorów lab
        :return: Wartości skośności luminacji i tinty
        """
        wynik = []
        wynik.append((np.sum((self.hist_l-self.mean_l)**3)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-self.mean_l)**2)/self.hist_l.size)**3))
        wynik.append((np.sum((self.hist_a-self.mean_a)**3)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-self.mean_a)**2)/self.hist_a.size)**3))
        return wynik

    def hist_kurt_rgb_rg(self) -> List:
        """
        Metoda służąca do obliczenia kurtozy w przestrzeni kolorów rgb
        :return: Wartości kurtozy kolorów czerwonego i zielonego
        """
        wynik = []
        wynik.append((np.sum((self.hist_r-self.mean_r)**4)/self.hist_r.size)/math.sqrt((np.sum((self.hist_r-self.mean_r)**2)/self.hist_r.size)**4)-3)
        wynik.append((np.sum((self.hist_g-self.mean_g)**4)/self.hist_g.size)/math.sqrt((np.sum((self.hist_g-self.mean_g)**2)/self.hist_g.size)**4)-3)
        return wynik

    def hist_kurt_hsv_sv(self) -> List:
        """
        Metoda służąca do obliczenia kurtozy w przestrzeni kolorów hsv
        :return: Wartości kurtozy nasycenia i wartości
        """
        wynik = []
        wynik.append((np.sum((self.hist_s-self.mean_s)**4)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-self.mean_s)**2)/self.hist_s.size)**4)-3)
        wynik.append((np.sum((self.hist_v-self.mean_v)**4)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-self.mean_v)**2)/self.hist_v.size)**4)-3)
        return wynik

    def hist_kurt_lab_la(self) -> List:
        """
        Metoda służąca do obliczenia kurtozy w przestrzeni kolorów lab
        :return: Wartości kurtozy luminacji i tinty
        """
        wynik = []
        wynik.append((np.sum((self.hist_l-self.mean_l)**4)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-self.mean_l)**2)/self.hist_l.size)**4)-3)
        wynik.append((np.sum((self.hist_a-self.mean_a)**4)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-self.mean_a)**2)/self.hist_a.size)**4)-3)
        return wynik

    def entropia_rgb_g(self) -> float:
        """
        Metoda służąca do obliczenia kurtozy w przestrzeni kolorów rgb
        :return: Wartość entropii koloru zielonego
        """
        wynik = shannon_entropy(self.obr[:, :, 1])
        return wynik

    def entropia_hsv_v(self) -> float:
        """
        Metoda służąca do obliczenia kurtozy w przestrzeni kolorów hsv
        :return: Wartość entropii wartości
        """
        hsv_obr = skimage.color.rgb2hsv(self.obr)
        wynik = shannon_entropy(hsv_obr[:, :, 2])
        return wynik

    def entropia_lab_lb(self) -> List:
        """
        Metoda służąca do obliczenia kurtozy w przestrzeni kolorów lab
        :return: Wartości entropii luminacji i temperatury
        """
        lab_obr = skimage.color.rgb2lab(self.obr, "D65", "2")
        wynik = []
        wynik.append(shannon_entropy(lab_obr[:, :, 0]))
        wynik.append(shannon_entropy(lab_obr[:, :, 2]))
        return wynik
