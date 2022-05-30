import math
import numpy as np
import skimage.io
import skimage.color
from skimage.measure.entropy import shannon_entropy


# klasa do generacji cech histogramów
# obraz i maska jako argumenty do konstruktora, zmien_obraz aby zmienić obraz/maske
# obraz = scieżka do pliku/numpy array
# maska = maska (numpy bool array uzyskany z Thresholding)
class CechyHistogram:
    def __init__(self, obraz, maska) -> None:
        self.obr = obraz
        self.maska = maska
        self.__obl_hist()

    def zmien_obraz(self, obraz, maska):
        if type(obraz) == str:
            self.obr = skimage.io.imread(obraz)
        else:
            self.obr = obraz
        self.maska = maska
        self.__obl_hist()

    # wylicza histogramy, wywoływane w konstruktorze/zmien_obraz
    def __obl_hist(self):
        r = self.obr[:, :, 0]  # czerwony
        g = self.obr[:, :, 1]  # zielony
        # b = self.obr[:, :, 2]  # niebieski
        self.hist_r, bin_brzegi_r = np.histogram(r[self.maska], bins=256, range=(0, 256))
        self.hist_g, bin_brzegi_g = np.histogram(g[self.maska], bins=256, range=(0, 256))
        # self.hist_b, bin_brzegi_b = np.histogram(b[self.maska], bins=256, range=(0, 256))
        self.mids_r = bin_brzegi_r[:-1]
        self.mids_g = bin_brzegi_g[:-1]
        # self.mids_b = bin_brzegi_b[:-1]

        hsv_obr = skimage.color.rgb2hsv(self.obr)
        # h = hsv_obr[:, :, 0]  # odcien
        s = hsv_obr[:, :, 1]  # nasycenie
        v = hsv_obr[:, :, 2]  # wartosc
        # self.hist_h, bin_brzegi_h = np.histogram(h[self.maska], bins=100, range=(0, 1))
        self.hist_s, bin_brzegi_s = np.histogram(s[self.maska], bins=100, range=(0, 1))
        self.hist_v, bin_brzegi_v = np.histogram(v[self.maska], bins=100, range=(0, 1))
        # self.mids_h = bin_brzegi_h[:-1]
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

        self.mean_r = np.average(self.mids_r, weights=self.hist_r)
        self.mean_g = np.average(self.mids_g, weights=self.hist_g)

        self.mean_s = np.average(self.mids_s, weights=self.hist_s)
        self.mean_v = np.average(self.mids_v, weights=self.hist_v)

        self.mean_l = np.average(self.mids_l, weights=self.hist_l)
        self.mean_a = np.average(self.mids_a, weights=self.hist_a)

    # zwraca średnią histogramów na kanale [G]
    def hist_srednia_rgb_g(self):
        wynik = self.mean_g
        return wynik

    # zwraca średnią histogramów na kanałach [S,V]
    def hist_srednia_hsv_sv(self):
        return [self.mean_s, self.mean_v]

    # zwraca średnią histogramów na kanale [L]
    def hist_srednia_lab_l(self):
        return self.mean_l

    # zwraca wariancje histogramów na każdym kanale [R,G,B]
    def hist_var_rgb_rg(self):
        wynik = []
        wynik.append(np.average((self.mids_r - self.mean_r)**2, weights=self.hist_r))
        wynik.append(np.average((self.mids_g - self.mean_g)**2, weights=self.hist_g))
        return wynik

    # zwraca wariancje histogramów na kanale [V]
    def hist_var_hsv_v(self):
        wynik = np.average((self.mids_v - self.mean_v)**2, weights=self.hist_v)
        return wynik

    # zwraca wariancje histogramów na kanalach [L,a*]
    def hist_var_lab_la(self):
        wynik = []
        wynik.append(np.average((self.mids_l - self.mean_l)**2, weights=self.hist_l))
        wynik.append(np.average((self.mids_a - self.mean_a)**2, weights=self.hist_a))
        return wynik

    # zwraca skośność histogramu na kanałach [R,G]
    def hist_skos_rgb_rg(self):
        wynik = []
        wynik.append((np.sum((self.hist_r-self.mean_r)**3)/self.hist_r.size)/math.sqrt((np.sum((self.hist_r-self.mean_r)**2)/self.hist_r.size)**3))
        wynik.append((np.sum((self.hist_g-self.mean_g)**3)/self.hist_g.size)/math.sqrt((np.sum((self.hist_g-self.mean_g)**2)/self.hist_g.size)**3))
        return wynik

    # zwraca skośność histogramu na kanałach [S,V]
    def hist_skos_hsv_sv(self):
        wynik = []
        wynik.append((np.sum((self.hist_s-self.mean_s)**3)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-self.mean_s)**2)/self.hist_s.size)**3))
        wynik.append((np.sum((self.hist_v-self.mean_v)**3)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-self.mean_v)**2)/self.hist_v.size)**3))
        return wynik

    # zwraca skośność histogramu na kanałach [L,a*]
    def hist_skos_lab_la(self):
        wynik = []
        wynik.append((np.sum((self.hist_l-self.mean_l)**3)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-self.mean_l)**2)/self.hist_l.size)**3))
        wynik.append((np.sum((self.hist_a-self.mean_a)**3)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-self.mean_a)**2)/self.hist_a.size)**3))
        return wynik

    # zwraca kurtoze histogramu na kanałach [R,G]
    def hist_kurt_rgb_rg(self):
        wynik = []
        wynik.append((np.sum((self.hist_r-self.mean_r)**4)/self.hist_r.size)/math.sqrt((np.sum((self.hist_r-self.mean_r)**2)/self.hist_r.size)**4)-3)
        wynik.append((np.sum((self.hist_g-self.mean_g)**4)/self.hist_g.size)/math.sqrt((np.sum((self.hist_g-self.mean_g)**2)/self.hist_g.size)**4)-3)
        return wynik

    # zwraca kurtoze histogramu na kanałach [S,V]
    def hist_kurt_hsv_sv(self):
        wynik = []
        wynik.append((np.sum((self.hist_s-self.mean_s)**4)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-self.mean_s)**2)/self.hist_s.size)**4)-3)
        wynik.append((np.sum((self.hist_v-self.mean_v)**4)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-self.mean_v)**2)/self.hist_v.size)**4)-3)
        return wynik

    # zwraca kurtoze histogramu na kanałach [L,a*]
    def hist_kurt_lab_la(self):
        wynik = []
        wynik.append((np.sum((self.hist_l-self.mean_l)**4)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-self.mean_l)**2)/self.hist_l.size)**4)-3)
        wynik.append((np.sum((self.hist_a-self.mean_a)**4)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-self.mean_a)**2)/self.hist_a.size)**4)-3)
        return wynik

    # zwraca entropie obrazu w RGB (float)
    def entropia_rgb_g(self):
        wynik = shannon_entropy(self.obr[:, :, 1])
        return wynik

    # zwraca entropie obrazu w HSV (float)
    def entropia_hsv_v(self):
        hsv_obr = skimage.color.rgb2hsv(self.obr)
        wynik = shannon_entropy(hsv_obr[:, :, 2])
        return wynik

    # zwraca entropie obrazu w La*b* (float)
    def entropia_lab_lb(self):
        lab_obr = skimage.color.rgb2lab(self.obr, "D65", "2")
        wynik = []
        wynik.append(shannon_entropy(lab_obr[:, :, 0]))
        wynik.append(shannon_entropy(lab_obr[:, :, 2]))
        return wynik
