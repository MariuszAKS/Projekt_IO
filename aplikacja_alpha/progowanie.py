import skimage.io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte


# klasa do generacji maski uzywajac OTSU
# konwertuje obraz do skali szarosci (grayscale), znajduje prog (threshold(float)) i generuje maske

class ProgowanieOTSU:
    def __init__(self) -> None:
        pass

    # zwraca maske w postaci numpy array
    # obraz = sciezka do pliku/numpy array
    def maska(self, obraz):
        if type(obraz) == str:
            skala_szarosci = rgb2gray(skimage.io.imread(fname=obraz))
        else:
            skala_szarosci = rgb2gray(obraz)

        prog = threshold_otsu(skala_szarosci)
        wynik = skala_szarosci <= prog
        return wynik

    # generuje maske i zapisuje do png (true=255, false=0)
    # obraz = sciezka do pliku/numpy array
    # sciezka_wynik = sciezka do zapisu
    def zapisz_maske(self, obraz, sciezka_wynik):
        wynik = self.maska(obraz)
        skimage.io.imsave(sciezka_wynik, img_as_ubyte(wynik))
        return wynik
