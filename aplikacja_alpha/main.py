"""
@package docstring
"""
from enum import Enum

from aplikacja_alpha.generowanie_cech import generowanie_cech
from aplikacja_alpha.klasyfikacja_obrazu import klasyfikacja


class Rodzaj(Enum):
    Bradyrhizobium = 1
    Enterobacter = 2
    Pantoea = 3
    Pseudomonas = 4
    Rhizobium = 5

    def __str__(self):
        return str(self.name)


def klasyfikuj(sciezka_do_pliku: str) -> Rodzaj:
    """
    Metoda wywołująca metody do obliczenia cech i klasyfikacji obrazu
    :return: Rodzaj bakterii w postaci str
    """
    cechy = generowanie_cech(sciezka_do_pliku)
    rodzaj = klasyfikacja([cechy])

    return Rodzaj(rodzaj)
