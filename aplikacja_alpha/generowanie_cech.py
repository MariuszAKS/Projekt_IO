import skimage.io
import csv

from aplikacja_alpha.progowanie import ProgowanieOTSU
from aplikacja_alpha.klasteryzacja import KlastryKSrednich
from aplikacja_alpha.kolorymetryczne import CechyKolorymetryczne
from aplikacja_alpha.histogram import CechyHistogram
from aplikacja_alpha.krawedzie import Krawedzie



def generowanie_cech(sciezka_do_pliku):
    # print('0. Generacja cech i segregowanie')
    # print('ROI: Segmentacja regionow zainteresowania (maska)')

    obraz = skimage.io.imread(sciezka_do_pliku)
    obraz_maska = ProgowanieOTSU()
    maska = obraz_maska.maska(sciezka_do_pliku)
    # maska = obraz_maska.zapisz_maske(obraz, 'maska.png')


    # print('Cechy: Klasteryzacja')

    obraz_klasteryzacja = KlastryKSrednich(obraz)
    centroidy_a, centroidy_b = obraz_klasteryzacja.centroidy()

    cecha_trzecia_centroida_b = centroidy_b[2][0]


    # print('Cechy: Kolorymetryczne')

    obraz_kolorymetryczne = CechyKolorymetryczne(obraz, maska)

    kolor_srednia_rgb = obraz_kolorymetryczne.srednia_rgb()
    kolor_srednia_hsv = obraz_kolorymetryczne.srednia_hsv()
    kolor_srednia_lab = obraz_kolorymetryczne.srednia_lab()
    kolor_std_rgb = obraz_kolorymetryczne.std_rgb()
    kolor_std_hsv = obraz_kolorymetryczne.std_hsv()
    kolor_std_lab = obraz_kolorymetryczne.std_lab()

    cecha_srednia_rgb_zielony = kolor_srednia_rgb[1]
    cecha_srednia_hsv_nasycenie = kolor_srednia_hsv[1]
    cecha_srednia_hsv_wartosc = kolor_srednia_hsv[2]
    cecha_srednia_lab_luminacja = kolor_srednia_lab[0]
    cecha_std_rgb_czerwony = kolor_std_rgb[0]
    cecha_std_rgb_zielony = kolor_std_rgb[1]
    cecha_std_rgb_niebieski = kolor_std_rgb[2]
    cecha_std_hsv_wartosc = kolor_std_hsv[2]
    cecha_std_lab_luminacja = kolor_std_lab[0]
    cecha_std_lab_tienta = kolor_std_lab[1]


    # print('Cechy: Histogram')

    obraz_histogram = CechyHistogram(obraz, maska)
    hist_srednia_rgb = obraz_histogram.hist_srednia_rgb()
    hist_srednia_hsv = obraz_histogram.hist_srednia_hsv()
    hist_srednia_lab = obraz_histogram.hist_srednia_lab()
    hist_wariancja_rgb = obraz_histogram.hist_var_rgb()
    hist_wariancja_hsv = obraz_histogram.hist_var_hsv()
    hist_wariancja_lab = obraz_histogram.hist_var_lab()
    hist_skosnosc_rgb = obraz_histogram.hist_skos_rgb()
    hist_skosnosc_hsv = obraz_histogram.hist_skos_hsv()
    hist_skosnosc_lab = obraz_histogram.hist_skos_lab()
    hist_kurtoza_rgb = obraz_histogram.hist_kurt_rgb()
    hist_kurtoza_hsv = obraz_histogram.hist_kurt_hsv()
    hist_kurtoza_lab = obraz_histogram.hist_kurt_lab()
    hist_entropia_rgb = obraz_histogram.entropia_rgb()
    hist_entropia_hsv = obraz_histogram.entropia_hsv()
    hist_entropia_lab = obraz_histogram.entropia_lab()

    cecha_hist_srednia_rgb_zielony = hist_srednia_rgb[1]
    cecha_hist_srednia_hsv_nasycenie = hist_srednia_hsv[1]
    cecha_hist_srednia_hsv_wartosc = hist_srednia_hsv[2]
    cecha_hist_srednia_lab_luminacja = hist_srednia_lab[0]

    cecha_hist_wariancja_rgb_czerwony = hist_wariancja_rgb[0]
    cecha_hist_wariancja_rgb_zielony = hist_wariancja_rgb[1]
    cecha_hist_wariancja_hsv_wartosc = hist_wariancja_hsv[2]
    cecha_hist_wariancja_lab_luminacja = hist_wariancja_lab[0]
    cecha_hist_wariancja_lab_tienta = hist_wariancja_lab[1]

    cecha_hist_skosnosc_rgb_czerwony = hist_skosnosc_rgb[0]
    cecha_hist_skosnosc_rgb_zielony = hist_skosnosc_rgb[1]
    cecha_hist_skosnosc_hsv_nasycenie = hist_skosnosc_hsv[1]
    cecha_hist_skosnosc_hsv_wartosc = hist_skosnosc_hsv[2]
    cecha_hist_skosnosc_lab_luminacja = hist_skosnosc_lab[0]
    cecha_hist_skosnosc_lab_tienta = hist_skosnosc_lab[1]

    cecha_hist_kurtoza_rgb_czerwony = hist_kurtoza_rgb[0]
    cecha_hist_kurtoza_rgb_zielony = hist_kurtoza_rgb[1]
    cecha_hist_kurtoza_hsv_nasycenie = hist_kurtoza_hsv[1]
    cecha_hist_kurtoza_hsv_wartosc = hist_kurtoza_hsv[2]
    cecha_hist_kurtoza_lab_luminacja = hist_kurtoza_lab[0]
    cecha_hist_kurtoza_lab_tienta = hist_kurtoza_lab[1]

    cecha_hist_entropia_rgb_zielony = hist_entropia_rgb[1]
    cecha_hist_entropia_hsv_wartosc = hist_entropia_hsv[2]
    cecha_hist_entropia_lab_luminacja = hist_entropia_lab[0]
    cecha_hist_entropia_lab_temperatura = hist_entropia_lab[2]


    # print('Cechy: Krawedzie')

    obraz_krawedzie = Krawedzie(obraz)
    krawedzie_srednia_rgb = obraz_krawedzie.sredni_kolor_krawedzi_rgb()
    krawedzie_std_rgb = obraz_krawedzie.std_kolor_krawedzi_rgb()

    cecha_krawedzie_srednia_rgb_czerwony = krawedzie_srednia_rgb[0]
    cecha_krawedzie_std_czerwony = krawedzie_std_rgb[0]
    cecha_krawedzie_std_zielony = krawedzie_std_rgb[1]
    cecha_krawedzie_std_niebieski = krawedzie_std_rgb[2]


    # print('Gotowe')

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


    # print('Posegregowane')
    # print(cechy)

    return cechy

