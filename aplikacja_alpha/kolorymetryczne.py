import numpy as np
import skimage.io
import skimage.color


# klasa do generacji cech kolorymetrycznych
# obraz i maska jako argumenty do konstruktora, zmien_obraz aby zmienić obraz/maske
# obraz = ścieżka do pliku/numpy array
# maska = maska (numpy bool array from Thresholding)
class CechyKolorymetryczne:
    def __init__(self, obraz, maska) -> None:
        self.obraz = obraz
        self.maska = maska

    def zmien_obraz(self, obraz, maska):
        if type(obraz) == str:
            self.obraz = skimage.io.imread(obraz)
        else:
            self.obraz = obraz
        self.maska = maska

    # zwraca średnią pikseli na kanale [G]
    def srednia_rgb_g(self):
        wartosc = 0.0
        licznik = 0
        for i in range(0, self.obraz.shape[0]):
            for j in range(0, self.obraz.shape[1]):
                if self.maska[i, j]:
                    wartosc += self.obraz[i, j, 1]
                    licznik += 1
        wynik = wartosc/licznik
        return wynik

    # zwraca średnią pikseli na kanałach [S,V]
    def srednia_hsv_sv(self):
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

    # zwraca średnią pikseli na kanale [L]
    def srednia_lab_l(self):
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

    # zwraca odchylenie standardowe na kazdym kanale [R,G,B]
    def std_rgb(self):
        wynik = []
        r = self.obraz[:, :, 0]  # czerwony
        g = self.obraz[:, :, 1]  # zielony
        b = self.obraz[:, :, 2]  # niebieski

        wynik.append(np.std(r[self.maska]))
        wynik.append(np.std(g[self.maska]))
        wynik.append(np.std(b[self.maska]))
        return wynik

    # zwraca odchylenie standardowe na kanale [V]
    def std_hsv_v(self):
        hsv_obr = skimage.color.rgb2hsv(self.obraz)
        v = hsv_obr[:, :, 2]  # wartosc

        wynik = np.std(v[self.maska])
        return wynik

    # zwraca odchylenie standardowe na kanalach [L,a*]
    def std_lab_la(self):
        lab_obr = skimage.color.rgb2lab(self.obraz, "D65", "2")
        wynik = []
        l = lab_obr[:, :, 0]  # luminacja
        a = lab_obr[:, :, 1]  # tienta

        wynik.append(np.std(l[self.maska]))
        wynik.append(np.std(a[self.maska]))
        return wynik
