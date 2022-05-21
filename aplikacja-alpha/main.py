import generowanie_cech as gc
import klasyfikacja_obrazu as ko
from enum import Enum


class Rodzaje(Enum):
    Bradyrhizobium = 1
    Enterobacter = 2
    Pantoea = 3
    Pseudomonas = 4
    Rhizobium = 5


def klasyfikuj(sciezka_do_pliku):
    # Wygeneruj cechy wskazanego obrazu
    cechy = gc.generowanie_cech(sciezka_do_pliku)
    print('Cechy wygenerowane')

    # Zwróć wartość numeryczną (według pliku z cechami) wybranego rodzaju
    return ko.klasyfikacja([cechy])


print(Rodzaje(klasyfikuj('obraz.png')).name)
