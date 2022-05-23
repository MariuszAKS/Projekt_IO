from aplikacja_alpha.generowanie_cech import generowanie_cech
from aplikacja_alpha.klasyfikacja_obrazu import klasyfikacja
from enum import Enum


class Rodzaj(Enum):
    Bradyrhizobium = 1
    Enterobacter = 2
    Pantoea = 3
    Pseudomonas = 4
    Rhizobium = 5

    def __str__(self):
        return str(self.name)



def klasyfikuj(sciezka_do_pliku: str) -> str:
    # Wygeneruj cechy wskazanego obrazu
    cechy = generowanie_cech(sciezka_do_pliku)

    return str(Rodzaj(klasyfikacja([cechy])))


# print(klasyfikuj('obraz.png'))
