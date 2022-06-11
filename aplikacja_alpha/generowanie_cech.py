from math import isnan
import numpy as np
import skimage.io

from typing import List

from aplikacja_alpha.progowanie import ProgowanieOTSU
from aplikacja_alpha.klasteryzacja import KlastryKSrednich
from aplikacja_alpha.kolorymetryczne import CechyKolorymetryczne
from aplikacja_alpha.histogram import CechyHistogram
from aplikacja_alpha.krawedzie import Krawedzie

# Metoda generująca cechy z obrazu
# zwracająca posegregowane cechy

def generowanie_cech(sciezka_do_pliku: str) -> List[float]:
    print('0. Generacja cech i segregowanie')
    print('ROI: Segmentacja regionow zainteresowania (maska)')
    
    obraz_0 = skimage.io.imread(sciezka_do_pliku)
    
    if len(obraz_0.shape) > 2:
        obraz = obraz_0[:, :, :3]
    else:
        obraz = np.ndarray(shape=(obraz_0.shape[0], obraz_0.shape[1], 3))
        for i in range(0, obraz_0.shape[0]):
            for j in range(0, obraz_0.shape[1]):
                wartosc = obraz_0[i][j]
                obraz[i][j][0] = wartosc
                obraz[i][j][1] = wartosc
                obraz[i][j][2] = wartosc
    
    # generuję maskę używając OTSU
    obraz_maska = ProgowanieOTSU()
    maska = obraz_maska.maska(obraz)
    # maska = obraz_maska.zapisz_maske(obraz, 'maska.png')
    
    print('Cechy: Klasteryzacja')
    
    obraz_klasteryzacja = KlastryKSrednich(obraz)
    centroidy_b = obraz_klasteryzacja.centroidy_b()

    cecha_trzecia_centroida_b = centroidy_b[2][0]

    print('Cechy: Kolorymetryczne')

    obraz_kolorymetryczne = CechyKolorymetryczne(obraz, maska)

    kolor_srednia_rgb_g = obraz_kolorymetryczne.srednia_rgb_g()
    kolor_srednia_hsv_sv = obraz_kolorymetryczne.srednia_hsv_sv()
    kolor_srednia_lab_l = obraz_kolorymetryczne.srednia_lab_l()
    kolor_std_rgb = obraz_kolorymetryczne.std_rgb()
    kolor_std_hsv_v = obraz_kolorymetryczne.std_hsv_v()
    kolor_std_lab_la = obraz_kolorymetryczne.std_lab_la()

    cecha_srednia_rgb_zielony = kolor_srednia_rgb_g
    cecha_srednia_hsv_nasycenie = kolor_srednia_hsv_sv[0]
    cecha_srednia_hsv_wartosc = kolor_srednia_hsv_sv[1]
    cecha_srednia_lab_luminacja = kolor_srednia_lab_l
    cecha_std_rgb_czerwony = kolor_std_rgb[0]
    cecha_std_rgb_zielony = kolor_std_rgb[1]
    cecha_std_rgb_niebieski = kolor_std_rgb[2]
    cecha_std_hsv_wartosc = kolor_std_hsv_v
    cecha_std_lab_luminacja = kolor_std_lab_la[0]
    cecha_std_lab_tienta = kolor_std_lab_la[1]

    print('Cechy: Histogram')

    obraz_histogram = CechyHistogram(obraz, maska)

    hist_srednia_rgb_g = obraz_histogram.hist_srednia_rgb_g()
    hist_srednia_hsv_sv = obraz_histogram.hist_srednia_hsv_sv()
    hist_srednia_lab_l = obraz_histogram.hist_srednia_lab_l()
    hist_wariancja_rgb_rg = obraz_histogram.hist_var_rgb_rg()
    hist_wariancja_hsv_v = obraz_histogram.hist_var_hsv_v()
    hist_wariancja_lab_la = obraz_histogram.hist_var_lab_la()
    hist_skosnosc_rgb_rg = obraz_histogram.hist_skos_rgb_rg()
    hist_skosnosc_hsv_sv = obraz_histogram.hist_skos_hsv_sv()
    hist_skosnosc_lab_la = obraz_histogram.hist_skos_lab_la()
    hist_kurtoza_rgb_rg = obraz_histogram.hist_kurt_rgb_rg()
    hist_kurtoza_hsv_sv = obraz_histogram.hist_kurt_hsv_sv()
    hist_kurtoza_lab_la = obraz_histogram.hist_kurt_lab_la()
    hist_entropia_rgb_g = obraz_histogram.entropia_rgb_g()
    hist_entropia_hsv_v = obraz_histogram.entropia_hsv_v()
    hist_entropia_lab_lb = obraz_histogram.entropia_lab_lb()

    cecha_hist_srednia_rgb_zielony = hist_srednia_rgb_g
    cecha_hist_srednia_hsv_nasycenie = hist_srednia_hsv_sv[0]
    cecha_hist_srednia_hsv_wartosc = hist_srednia_hsv_sv[1]
    cecha_hist_srednia_lab_luminacja = hist_srednia_lab_l

    cecha_hist_wariancja_rgb_czerwony = hist_wariancja_rgb_rg[0]
    cecha_hist_wariancja_rgb_zielony = hist_wariancja_rgb_rg[1]
    cecha_hist_wariancja_hsv_wartosc = hist_wariancja_hsv_v
    cecha_hist_wariancja_lab_luminacja = hist_wariancja_lab_la[0]
    cecha_hist_wariancja_lab_tienta = hist_wariancja_lab_la[1]

    cecha_hist_skosnosc_rgb_czerwony = hist_skosnosc_rgb_rg[0]
    cecha_hist_skosnosc_rgb_zielony = hist_skosnosc_rgb_rg[1]
    cecha_hist_skosnosc_hsv_nasycenie = hist_skosnosc_hsv_sv[0]
    cecha_hist_skosnosc_hsv_wartosc = hist_skosnosc_hsv_sv[1]
    cecha_hist_skosnosc_lab_luminacja = hist_skosnosc_lab_la[0]
    cecha_hist_skosnosc_lab_tienta = hist_skosnosc_lab_la[1]

    cecha_hist_kurtoza_rgb_czerwony = hist_kurtoza_rgb_rg[0]
    cecha_hist_kurtoza_rgb_zielony = hist_kurtoza_rgb_rg[1]
    cecha_hist_kurtoza_hsv_nasycenie = hist_kurtoza_hsv_sv[0]
    cecha_hist_kurtoza_hsv_wartosc = hist_kurtoza_hsv_sv[1]
    cecha_hist_kurtoza_lab_luminacja = hist_kurtoza_lab_la[0]
    cecha_hist_kurtoza_lab_tienta = hist_kurtoza_lab_la[1]

    cecha_hist_entropia_rgb_zielony = hist_entropia_rgb_g
    cecha_hist_entropia_hsv_wartosc = hist_entropia_hsv_v
    cecha_hist_entropia_lab_luminacja = hist_entropia_lab_lb[0]
    cecha_hist_entropia_lab_temperatura = hist_entropia_lab_lb[1]

    print('Cechy: Krawedzie')

    obraz_krawedzie = Krawedzie(obraz)
    krawedzie_srednia_rgb_r = obraz_krawedzie.sredni_kolor_krawedzi_rgb_r()
    krawedzie_std_rgb = obraz_krawedzie.std_kolor_krawedzi_rgb()

    cecha_krawedzie_srednia_rgb_czerwony = krawedzie_srednia_rgb_r
    cecha_krawedzie_std_czerwony = krawedzie_std_rgb[0]
    cecha_krawedzie_std_zielony = krawedzie_std_rgb[1]
    cecha_krawedzie_std_niebieski = krawedzie_std_rgb[2]

    print('Cechy wygenerowane')
    
    #dodaję cechy według danej kolejności w obrazie
    cechy = []
    cechy.append(cecha_hist_wariancja_lab_tienta)
    cechy.append(cecha_std_lab_tienta)
    cechy.append(cecha_krawedzie_std_zielony)
    cechy.append(cecha_hist_wariancja_lab_luminacja)
    cechy.append(cecha_std_lab_luminacja)

    cechy.append(cecha_std_rgb_zielony)
    cechy.append(cecha_hist_wariancja_rgb_zielony)
    cechy.append(cecha_hist_skosnosc_rgb_czerwony)
    cechy.append(cecha_hist_kurtoza_rgb_czerwony)
    cechy.append(cecha_trzecia_centroida_b)

    cechy.append(cecha_hist_kurtoza_lab_luminacja)
    cechy.append(cecha_std_rgb_czerwony)
    cechy.append(cecha_hist_wariancja_rgb_czerwony)
    cechy.append(cecha_krawedzie_std_niebieski)
    cechy.append(cecha_hist_skosnosc_rgb_zielony)

    cechy.append(cecha_hist_kurtoza_hsv_wartosc)
    cechy.append(cecha_hist_skosnosc_hsv_wartosc)
    cechy.append(cecha_hist_skosnosc_lab_luminacja)
    cechy.append(cecha_hist_kurtoza_rgb_zielony)
    cechy.append(cecha_srednia_hsv_nasycenie)

    cechy.append(cecha_hist_kurtoza_hsv_nasycenie)
    cechy.append(cecha_hist_srednia_hsv_nasycenie)
    cechy.append(cecha_hist_skosnosc_hsv_nasycenie)
    cechy.append(cecha_hist_skosnosc_lab_tienta)
    cechy.append(cecha_hist_kurtoza_lab_tienta)

    cechy.append(cecha_hist_srednia_rgb_zielony)
    cechy.append(cecha_std_hsv_wartosc)
    cechy.append(cecha_srednia_rgb_zielony)
    cechy.append(cecha_hist_wariancja_hsv_wartosc)
    cechy.append(cecha_hist_srednia_hsv_wartosc)

    cechy.append(cecha_srednia_lab_luminacja)
    cechy.append(cecha_srednia_hsv_wartosc)
    cechy.append(cecha_std_rgb_niebieski)
    cechy.append(cecha_krawedzie_srednia_rgb_czerwony)
    cechy.append(cecha_hist_srednia_lab_luminacja)

    cechy.append(cecha_hist_entropia_rgb_zielony)
    cechy.append(cecha_hist_entropia_hsv_wartosc)
    cechy.append(cecha_hist_entropia_lab_luminacja)
    cechy.append(cecha_hist_entropia_lab_temperatura)
    cechy.append(cecha_krawedzie_std_czerwony)
    
    #sprawdzam czy i-ta cecha nie ma wartości NaN
    for i in range(0, len(cechy)):
        if isnan(cechy[i]):
            cechy[i] = 0.0
    
    print('Cechy posegregowane')
    # print(cechy)

    return cechy

