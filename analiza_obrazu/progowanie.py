import skimage.io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte


# klasa do generacji maski używając OTSU
# konwertuje obraz do skali szarości (grayscale), znajduje próg (threshold(float)) i generuje maskę

class ProgowanieOTSU:
    def __init__(self) -> None:
        pass

    # zwraca maskę w postaci numpy array
    # obraz = ścieżka do pliku/numpy array
    def maska(self, obraz):
        if type(obraz) == str:
            skala_szarosci = rgb2gray(skimage.io.imread(fname=obraz))
        else:
            skala_szarosci = rgb2gray(obraz)

        prog = threshold_otsu(skala_szarosci)
        wynik = skala_szarosci <= prog
        return wynik

    # generuje maskę i zapisuje do png (true=255, false=0)
    # obraz = ścieżka do pliku/numpy array
    # sciezka_wynik = ścieżka do zapisu
    def zapisz_maske(self, obraz, sciezka_wynik):
        wynik = self.maska(obraz)
        skimage.io.imsave(sciezka_wynik, img_as_ubyte(wynik))
        return wynik
    
