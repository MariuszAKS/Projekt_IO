import math
import numpy as np
import skimage.io
import skimage.color
from skimage.measure.entropy import shannon_entropy
from skimage.color import rgb2gray
from skimage.feature import canny
from sklearn.cluster import KMeans
from skimage.util import img_as_ubyte
from skimage.color import rgb2lab

class KlastryKSrednich:

    def __init__(self, obraz) -> None:
        if type(obraz) == str:
            self.obr = rgb2lab(skimage.io.imread(obraz), "D65", "2")
        else:
            self.obr = rgb2lab(obraz, "D65", "2")
        self.__obl_klastry()

    def zmien_obraz(self, obraz):
        if type(obraz) == str:
            self.obr = rgb2lab(skimage.io.imread(obraz), "D65", "2")
        else:
            self.obr = rgb2lab(obraz, "D65", "2")
        self.__obl_klastry()

    # trenuje modele k-means
    # wywoływane w konstruktorze/zmien_obraz
    def __obl_klastry(self):
        a = np.array([[x] for x in self.obr[:, :, 1].flatten()])
        b = np.array([[x] for x in self.obr[:, :, 2].flatten()])
        self.k_srednich_a = KMeans(n_clusters=3).fit(a)
        self.k_srednich_b = KMeans(n_clusters=3).fit(b)

    # zwraca centroid każdego klastara ([[a*1],[a*2],[a*3]],[[b*1],[b*2],[b*3]])
    def centroidy(self):
        return (self.k_srednich_b.cluster_centers_)

    # zapisuje wizualizacje klastrów
    # sciezka_wynik = ścieżka do pliku
    def zapisz_klaster_obraz_b(self, sciezka_wynik):
        kl = self.k_srednich_b.labels_
        kl = np.reshape(kl, (self.obr.shape[0], self.obr.shape[1])) * 127
        skimage.io.imsave(sciezka_wynik, img_as_ubyte(kl), check_contrast=False)

class Krawedzie:
    def __init__(self, obraz) -> None:
        if type(obraz) == str:
            self.obr_kolor = skimage.io.imread(obraz)
            obr = rgb2gray(self.obr_kolor)
        else:
            self.obr_kolor = obraz
            obr = rgb2gray(self.obr_kolor)
        self.maska_krawedzi = canny(obr, sigma=1)

    def zmien_obraz(self, obraz):
        if type(obraz) == str:
            self.obr_kolor = skimage.io.imread(obraz)
            obr = rgb2gray(self.obr_kolor)
        else:
            self.obr_kolor = obraz
            obr = rgb2gray(self.obr_kolor)
        self.maska_krawedzi = canny(obr, sigma=1)

    # zwraca maskę krawędzi (2d numpy bool array)
    def maska(self):
        return self.maska_krawedzi

    # zwraca średni kolor krawędzi dla każdego kanału [czerwony,zielony,niebieski]
    def sredni_kolor_krawedzi_rgb(self):
        r = self.obr_kolor[:, :, 0]  # czerwony
        g = self.obr_kolor[:, :, 1]  # zielony
        b = self.obr_kolor[:, :, 2]  # niebieski
        return [r[self.maska_krawedzi].mean(), g[self.maska_krawedzi].mean(), b[self.maska_krawedzi].mean()]

    # zwraca odchylenie standardowe koloru krawędzi dla każdego kanału [czerwony,zielony,niebieski]
    def std_kolor_krawedzi_rgb(self):
        r = self.obr_kolor[:, :, 0]  # czerwony
        g = self.obr_kolor[:, :, 1]  # zielony
        b = self.obr_kolor[:, :, 2]  # niebieski
        return [r[self.maska_krawedzi].std(), g[self.maska_krawedzi].std(), b[self.maska_krawedzi].std()]
    
class CechyKolorymetryczne:
    
    def __init__(self, obraz, maska) -> None:
        if type(obraz) == str:
            self.obraz = skimage.io.imread(obraz)
        else:
            self.obraz = obraz
        self.maska = maska

    def zmien_obraz(self, obraz, maska):
        if type(obraz) == str:
            self.obraz = skimage.io.imread(obraz)
        else:
            self.obraz = obraz
        self.maska = maska

    # zwraca średnią pikseli na każdym kanale [R,G,B]
    def srednia_rgb(self):

        wynik = []
        for channel in range(0, 3):
            wartosc = 0.0
            licznik = 0
            for i in range(0, self.obraz.shape[0]):
                for j in range(0, self.obraz.shape[1]):
                    if self.maska[i, j]:
                        wartosc += self.obraz[i, j, channel]
                        licznik += 1
            wynik.append(wartosc/licznik)
        return wynik

    # zwraca średnią pikseli na każdym kanale [H,S,V]
    def srednia_hsv(self):
        hsv_obr = skimage.color.rgb2hsv(self.obraz)
        wynik = []
        for kanal in range(0, 3):
            wartosc = 0.0
            licznik = 0
            for i in range(0, hsv_obr.shape[0]):
                for j in range(0, hsv_obr.shape[1]):
                    if self.maska[i, j]:
                        wartosc += hsv_obr[i, j, kanal]
                        licznik += 1
            wynik.append(wartosc/licznik)
        return wynik

    # zwraca średnią pikseli na każdym kanale [L,a*,b*]
    def srednia_lab(self):
        lab_obr = skimage.color.rgb2lab(self.obraz, "D65", "2")
        wynik = []
        for channel in range(0, 3):
            wartosc = 0.0
            licznik = 0
            for i in range(0, lab_obr.shape[0]):
                for j in range(0, lab_obr.shape[1]):
                    if self.maska[i, j]:
                        wartosc += lab_obr[i, j, channel]
                        licznik += 1
            wynik.append(wartosc/licznik)
        return wynik

    # zwraca odchylenie standardowe na każdym kanale [R,G,B]
    def std_rgb(self):
        wynik = []
        r = self.obraz[:, :, 0]  # czerwony
        g = self.obraz[:, :, 1]  # zielony
        b = self.obraz[:, :, 2]  # niebieski

        wynik.append(np.std(r[self.maska]))
        wynik.append(np.std(g[self.maska]))
        wynik.append(np.std(b[self.maska]))
        return wynik

    # zwraca odchylenie standardowe na każdym kanale [H,S,V]
    def std_hsv(self):
        hsv_obr = skimage.color.rgb2hsv(self.obraz)
        wynik = []
        h = hsv_obr[:, :, 0]  # odcień
        s = hsv_obr[:, :, 1]  # nasycenie
        v = hsv_obr[:, :, 2]  # wartość

        wynik.append(np.std(h[self.maska]))
        wynik.append(np.std(s[self.maska]))
        wynik.append(np.std(v[self.maska]))
        return wynik

    # zwraca odchylenie standardowe na każdym kanale [L,a*,b*]
    def std_lab(self):
        lab_obr = skimage.color.rgb2lab(self.obraz, "D65", "2")
        wynik = []
        l = lab_obr[:, :, 0]  # luminacja
        a = lab_obr[:, :, 1]  # tienta
        b = lab_obr[:, :, 2]  # temperatura

        wynik.append(np.std(l[self.maska]))
        wynik.append(np.std(a[self.maska]))
        wynik.append(np.std(b[self.maska]))
        return wynik
    
class CechyHistogram:
    def __init__(self, obraz, maska) -> None:
        if type(obraz) == str:
            self.obr = skimage.io.imread(obraz)
        else:
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
        b = self.obr[:, :, 2]  # niebieski
        self.hist_r, bin_brzegi_r = np.histogram(r[self.maska], bins=256, range=(0, 256))
        self.hist_g, bin_brzegi_g = np.histogram(g[self.maska], bins=256, range=(0, 256))
        self.hist_b, bin_brzegi_b = np.histogram(b[self.maska], bins=256, range=(0, 256))
        self.mids_r = bin_brzegi_r[:-1]
        self.mids_g = bin_brzegi_g[:-1]
        self.mids_b = bin_brzegi_b[:-1]

        hsv_obr = skimage.color.rgb2hsv(self.obr)
        h = hsv_obr[:, :, 0]  # odcień
        s = hsv_obr[:, :, 1]  # nasycenie
        v = hsv_obr[:, :, 2]  # wartość
        self.hist_h, bin_brzegi_h = np.histogram(h[self.maska], bins=100, range=(0, 1))
        self.hist_s, bin_brzegi_s = np.histogram(s[self.maska], bins=100, range=(0, 1))
        self.hist_v, bin_brzegi_v = np.histogram(v[self.maska], bins=100, range=(0, 1))
        self.mids_h = bin_brzegi_h[:-1]
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

    # zwraca średnią histogramów na każdym kanale [R,G,B]
    def hist_srednia_rgb(self):
        wynik = []
        wynik.append(np.average(self.mids_r, weights=self.hist_r))
        wynik.append(np.average(self.mids_g, weights=self.hist_g))
        wynik.append(np.average(self.mids_b, weights=self.hist_b))
        return wynik

    # zwraca średnią histogramów na każdym kanale [H,S,V]
    def hist_srednia_hsv(self):
        wynik = []
        wynik.append(np.average(self.mids_h, weights=self.hist_h))
        wynik.append(np.average(self.mids_s, weights=self.hist_s))
        wynik.append(np.average(self.mids_v, weights=self.hist_v))
        return wynik

    # zwraca średnią histogramów na każdym kanale [L,a*,b*]
    def hist_srednia_lab(self):
        wynik = []
        wynik.append(np.average(self.mids_l, weights=self.hist_l))
        wynik.append(np.average(self.mids_a, weights=self.hist_a))
        wynik.append(np.average(self.mids_b, weights=self.hist_b))
        return wynik

    # zwraca wariancje histogramów na każdym kanale [R,G,B]
    def hist_var_rgb(self):
        wynik = []
        srednia = self.hist_srednia_rgb()
        wynik.append(np.average((self.mids_r - srednia[0])**2, weights=self.hist_r))
        wynik.append(np.average((self.mids_g - srednia[1])**2, weights=self.hist_g))
        wynik.append(np.average((self.mids_b - srednia[2])**2, weights=self.hist_b))
        return wynik

    # zwraca wariancje histogramów na każdym kanale [H,S,V]
    def hist_var_hsv(self):
        wynik = []
        srednia = self.hist_srednia_hsv()
        wynik.append(np.average((self.mids_h - srednia[0])**2, weights=self.hist_h))
        wynik.append(np.average((self.mids_s - srednia[1])**2, weights=self.hist_s))
        wynik.append(np.average((self.mids_v - srednia[2])**2, weights=self.hist_v))
        return wynik

    # zwraca wariancje histogramów na każdym kanale [L,a*,b*]
    def hist_var_lab(self):
        wynik = []
        srednia = self.hist_srednia_lab()
        wynik.append(np.average((self.mids_l - srednia[0])**2, weights=self.hist_l))
        wynik.append(np.average((self.mids_a - srednia[1])**2, weights=self.hist_a))
        wynik.append(np.average((self.mids_b - srednia[2])**2, weights=self.hist_b))
        return wynik

    # zwraca skośność histogramu na każdym kanale [R,G,B]
    def hist_skos_rgb(self):
        wynik = []
        srednia = self.hist_srednia_rgb()
        wynik.append((np.sum((self.hist_r-srednia[0])**3)/self.hist_r.size)/math.sqrt((np.sum((self.hist_r-srednia[0])**2)/self.hist_r.size)**3))
        wynik.append((np.sum((self.hist_g-srednia[1])**3)/self.hist_g.size)/math.sqrt((np.sum((self.hist_g-srednia[1])**2)/self.hist_g.size)**3))
        wynik.append((np.sum((self.hist_b-srednia[2])**3)/self.hist_b.size)/math.sqrt((np.sum((self.hist_b-srednia[2])**2)/self.hist_b.size)**3))
        return wynik

    # zwraca skośność histogramu na każdym kanale [H,S,V]
    def hist_skos_hsv(self):
        wynik = []
        srednia = self.hist_srednia_hsv()
        wynik.append((np.sum((self.hist_h-srednia[0])**3)/self.hist_h.size)/math.sqrt((np.sum((self.hist_h-srednia[0])**2)/self.hist_h.size)**3))
        wynik.append((np.sum((self.hist_s-srednia[1])**3)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-srednia[1])**2)/self.hist_s.size)**3))
        wynik.append((np.sum((self.hist_v-srednia[2])**3)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-srednia[2])**2)/self.hist_v.size)**3))
        return wynik

    # zwraca skośność histogramu na każdym kanale [L,a*,b*]
    def hist_skos_lab(self):
        wynik = []
        srednia = self.hist_srednia_lab()
        wynik.append((np.sum((self.hist_l-srednia[0])**3)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-srednia[0])**2)/self.hist_l.size)**3))
        wynik.append((np.sum((self.hist_a-srednia[1])**3)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-srednia[1])**2)/self.hist_a.size)**3))
        wynik.append((np.sum((self.hist_b-srednia[2])**3)/self.hist_b.size)/math.sqrt((np.sum((self.hist_b-srednia[2])**2)/self.hist_b.size)**3))
        return wynik

    # zwraca kurtozę histogramu na każdym kanale [R,G,B]
    def hist_kurt_rgb(self):
        wynik = []
        srednia = self.hist_srednia_rgb()
        wynik.append((np.sum((self.hist_r-srednia[0])**4)/self.hist_r.size)/math.sqrt((np.sum((self.hist_r-srednia[0])**2)/self.hist_r.size)**4)-3)
        wynik.append((np.sum((self.hist_g-srednia[1])**4)/self.hist_g.size)/math.sqrt((np.sum((self.hist_g-srednia[1])**2)/self.hist_g.size)**4)-3)
        wynik.append((np.sum((self.hist_b-srednia[2])**4)/self.hist_b.size)/math.sqrt((np.sum((self.hist_b-srednia[2])**2)/self.hist_b.size)**4)-3)
        return wynik

    # zwraca kurtozę histogramu na każdym kanale [H,S,V]
    def hist_kurt_hsv(self):
        wynik = []
        srednia = self.hist_srednia_hsv()
        wynik.append((np.sum((self.hist_h-srednia[0])**4)/self.hist_h.size)/math.sqrt((np.sum((self.hist_h-srednia[0])**2)/self.hist_h.size)**4)-3)
        wynik.append((np.sum((self.hist_s-srednia[1])**4)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-srednia[1])**2)/self.hist_s.size)**4)-3)
        wynik.append((np.sum((self.hist_v-srednia[2])**4)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-srednia[2])**2)/self.hist_v.size)**4)-3)
        return wynik

    # zwraca kurtozę histogramu na każdym kanale [L,a*,b*]
    def hist_kurt_lab(self):
        wynik = []
        srednia = self.hist_srednia_lab()
        wynik.append((np.sum((self.hist_l-srednia[0])**4)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-srednia[0])**2)/self.hist_l.size)**4)-3)
        wynik.append((np.sum((self.hist_a-srednia[1])**4)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-srednia[1])**2)/self.hist_a.size)**4)-3)
        wynik.append((np.sum((self.hist_b-srednia[2])**4)/self.hist_b.size)/math.sqrt((np.sum((self.hist_b-srednia[2])**2)/self.hist_b.size)**4)-3)
        return wynik

    # zwraca entropie obrazu w RGB (float)
    def entropia_rgb(self):
        wynik = []
        wynik.append(shannon_entropy(self.obr[:, :, 0]))
        wynik.append(shannon_entropy(self.obr[:, :, 1]))
        wynik.append(shannon_entropy(self.obr[:, :, 2]))
        return wynik

    # zwraca entropie obrazu w HSV (float)
    def entropia_hsv(self):
        hsv_obr = skimage.color.rgb2hsv(self.obr)
        wynik = []
        wynik.append(shannon_entropy(hsv_obr[:, :, 0]))
        wynik.append(shannon_entropy(hsv_obr[:, :, 1]))
        wynik.append(shannon_entropy(hsv_obr[:, :, 2]))
        return wynik

    # zwraca entropie obrazu w La*b* (float)
    def entropia_lab(self):
        lab_obr = skimage.color.rgb2lab(self.obr, "D65", "2")
        wynik = []
        wynik.append(shannon_entropy(lab_obr[:, :, 0]))
        wynik.append(shannon_entropy(lab_obr[:, :, 1]))
        wynik.append(shannon_entropy(lab_obr[:, :, 2]))
        return wynik
